# Talking-photo animator: jaw drop warp driven by VO loudness + head sway + blinks.
import json, sys, os, numpy as np, cv2
from PIL import Image
TL=json.load(open('timeline.json'))
env=np.array(TL['env']); env=env/np.percentile(env[env>0],95); env=np.clip(env,0,1.2)
FPS=30
def mouth_curve(t0,t1):
    n=int(round((t1-t0)*FPS)); i0=int(round(t0*FPS))
    e=np.array([env[i0+k] if i0+k<len(env) else 0 for k in range(n)])
    # attack/release smoothing
    o=np.zeros(n); v=0
    for k in range(n):
        v=v+(e[k]-v)*(0.75 if e[k]>v else 0.45); o[k]=v
    return np.clip(o,0,1)
def run(name,src,S,seam,cx,halfw,lowlip,chin,amax,t0,t1,out,alpha_src=None):
    im=Image.open(src).convert('RGBA')
    im=im.resize((im.width*S,im.height*S),Image.LANCZOS)
    a=np.array(im).astype(np.float32)
    rgb=cv2.cvtColor(a[...,:3].astype(np.uint8),cv2.COLOR_RGB2BGR)
    blur=cv2.GaussianBlur(rgb,(0,0),2); rgb=cv2.addWeighted(rgb,1.5,blur,-0.5,0)  # unsharp after upscale
    a[...,:3]=cv2.cvtColor(rgb,cv2.COLOR_BGR2RGB)
    H,W=a.shape[:2]; seam*=S; cx*=S; halfw*=S; chin*=S; lowlip*=S; amax*=S
    xs=np.arange(W,dtype=np.float32); ys=np.arange(H,dtype=np.float32)
    dx=np.abs(xs-cx)/halfw
    wx=np.clip(1-np.clip(dx-0.55,0,None)/0.75,0,1); wx=wx*wx*(3-2*wx)   # smooth across mouth width
    wy=np.ones(H,np.float32); wy[ys<seam]=0
    fall=(ys-chin)/(0.35*(chin-seam)+1); wy=np.where(ys>chin,np.clip(1-fall,0,1),wy); wy=wy*wy*(3-2*wy)
    g=np.clip(1-dx**2,0,1)**0.8                     # lens-shaped lip opening across mouth width
    sy=np.clip((ys-lowlip)/(chin-lowlip),0,1); sy=sy*sy*(3-2*sy)
    G,SY=np.meshgrid(g,sy); WX,WY=np.meshgrid(wx,wy)
    PROF=G*(1-SY)+WX*SY
    X,Y=np.meshgrid(xs,ys)
    curve=mouth_curve(t0,t1); os.makedirs(out,exist_ok=True)
    for k,m in enumerate(curve):
        A=amax*m
        D=A*PROF*WY
        mapy=(Y-D).astype(np.float32)
        f=cv2.remap(a,X.astype(np.float32),mapy,cv2.INTER_CUBIC,borderMode=cv2.BORDER_REPLICATE)
        if A>0.3:
            gh=A*G
            depth=np.clip((Y-seam)/(gh+1e-3),0,1)
            mk=((Y>=seam)&(Y<seam+gh)).astype(np.float32)
            mk=cv2.GaussianBlur(mk,(0,0),S*0.9)
            dark=0.28+0.25*np.sin(depth*np.pi)**0   # multiply darkening, keeps some texture
            mul=1-mk*(1-0.3)
            f[...,:3]=f[...,:3]*mul[...,None]
            f[...,0]+=mk*18   # warm red tint of mouth interior
        f=np.clip(f,0,255).astype(np.uint8)
        Image.fromarray(f,'RGBA').save(f'{out}/{k:04d}.png',compress_level=1)
    print(name,len(curve),'frames')
if __name__=='__main__':
    L=TL['lines']; O=0.1
    base='/home/user/DRFI2/video/bofu15/talk'
    run('suit','suit.png',4,seam=178.5,cx=139,halfw=30,lowlip=190,chin=212,amax=7.5,t0=L[0][0],t1=L[0][1]+0.25,out=base+'_hook')
    run('lab','/home/user/DRFI2/video/assets/founder.png',3,seam=148.5,cx=179,halfw=30,lowlip=158,chin=188,amax=6.5,t0=L[3][0],t1=L[3][1]+0.2,out=base+'_offer')
