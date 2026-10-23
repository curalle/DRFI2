# Builds the CURALLE pilot RCT participant pack (PIS + ICF, English & Bahasa Melayu,
# honorarium acknowledgement, withdrawal form) -> CURALLE_RCT_PIS_ICF.pdf
# Text in [square brackets] is a placeholder for the study team to complete.
import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether, NextPageTemplate)

F = '/usr/share/fonts/truetype/liberation/LiberationSans-'
pdfmetrics.registerFont(TTFont('Sans', F + 'Regular.ttf'))
pdfmetrics.registerFont(TTFont('Sans-B', F + 'Bold.ttf'))
pdfmetrics.registerFont(TTFont('Sans-I', F + 'Italic.ttf'))
pdfmetrics.registerFont(TTFont('Sans-BI', F + 'BoldItalic.ttf'))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('Sans', normal='Sans', bold='Sans-B', italic='Sans-I', boldItalic='Sans-BI')
pdfmetrics.registerFont(TTFont('Sym', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))

INK = colors.HexColor('#1F1A2E'); PURPLE = colors.HexColor('#5B3594'); MUTED = colors.HexColor('#5A5468')
TINT = colors.HexColor('#F1ECF7'); RULE = colors.HexColor('#C9BEDD'); PH = colors.HexColor('#A1361F')

S = dict(
    title=ParagraphStyle('t', fontName='Sans-B', fontSize=15, leading=19, textColor=PURPLE, alignment=TA_CENTER, spaceAfter=2),
    sub=ParagraphStyle('s', fontName='Sans', fontSize=9.5, leading=13, textColor=MUTED, alignment=TA_CENTER, spaceAfter=10),
    h=ParagraphStyle('h', fontName='Sans-B', fontSize=10.5, leading=14, textColor=PURPLE, spaceBefore=9, spaceAfter=3),
    p=ParagraphStyle('p', fontName='Sans', fontSize=9.5, leading=13.2, textColor=INK, spaceAfter=4),
    li=ParagraphStyle('li', fontName='Sans', fontSize=9.5, leading=13.2, textColor=INK, leftIndent=12, bulletIndent=2, spaceAfter=2),
    cell=ParagraphStyle('c', fontName='Sans', fontSize=8.8, leading=11.5, textColor=INK),
    cellb=ParagraphStyle('cb', fontName='Sans-B', fontSize=8.8, leading=11.5, textColor=INK),
    small=ParagraphStyle('sm', fontName='Sans-I', fontSize=8.3, leading=11, textColor=MUTED, spaceAfter=4),
)

def ph(text):
    """Colour [placeholders] so the study team can find them."""
    text = re.sub(r'\[([^\]]+)\]', lambda m: f'<font color="#A1361F">[{m.group(1)}]</font>', text)
    return text.replace('☐', '<font name="Sym">☐</font>')

def P(t, st='p'): return Paragraph(ph(t), S[st])
def H(t): return Paragraph(ph(t), S['h'])
def UL(items): return [Paragraph(ph(i), S['li'], bulletText='•') for i in items]

def table(rows, widths, header=True, shade_first_col=False, row_heights=None):
    data = [[Paragraph(ph(c), S['cellb'] if (header and r == 0) else S['cell']) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, rowHeights=row_heights, repeatRows=1 if header else 0)
    st = [('GRID', (0, 0), (-1, -1), 0.5, RULE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
          ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5)]
    if header: st.append(('BACKGROUND', (0, 0), (-1, 0), TINT))
    if shade_first_col: st.append(('BACKGROUND', (0, 0), (0, -1), TINT))
    t.setStyle(TableStyle(st)); return t

W = A4[0] - 40 * mm   # text width

def sig_block(rows, lang='en'):
    lab = ('Signature', 'Name (CAPITALS)', 'NRIC / Passport No.', 'Date') if lang == 'en' else \
          ('Tandatangan', 'Nama (HURUF BESAR)', 'No. K/P / Pasport', 'Tarikh')
    out = []
    for who in rows:
        data = [[Paragraph(f'<b>{who}</b>', S['cell']), '', '', ''],
                [Paragraph(lab[0], S['cell']), '', Paragraph(lab[3], S['cell']), ''],
                [Paragraph(lab[1], S['cell']), '', Paragraph(lab[2], S['cell']), '']]
        t = Table(data, colWidths=[34 * mm, 58 * mm, 36 * mm, W - 128 * mm], rowHeights=[16, 26, 22])
        t.setStyle(TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), TINT),
                               ('LINEBELOW', (1, 1), (1, 2), 0.6, INK), ('LINEBELOW', (3, 1), (3, 2), 0.6, INK),
                               ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'), ('BOX', (0, 0), (-1, -1), 0.5, RULE)]))
        out += [KeepTogether(t), Spacer(1, 7)]
    return out

def tick_rows(items, initials='Initials'):
    data = [[Paragraph(ph(f'{i + 1}. {t}'), S['cell']), Paragraph(initials, S['cell'])] for i, t in enumerate(items)]
    t = Table(data, colWidths=[W - 26 * mm, 26 * mm])
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, RULE), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('TEXTCOLOR', (1, 0), (1, -1), MUTED), ('TOPPADDING', (0, 0), (-1, -1), 5),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
    return t

# ---------------------------------------------------------------- page frame
TITLE_EN = 'A pilot randomised, double-blind, vehicle-controlled study of a postbiotic-loaded glycerosomal cream (CURALLE) in adults with mild-to-moderate atopic dermatitis'
TITLE_BM = 'Kajian rintis rawak, dua-buta dan berkawalan vehikel bagi krim glycerosome berisi postbiotik (CURALLE) dalam kalangan dewasa dengan dermatitis atopik ringan hingga sederhana'
VERSION = 'Version / Versi [1.0] · [dd/mm/yyyy]'

def on_page(c, doc):
    c.saveState()
    c.setFont('Sans-B', 8); c.setFillColor(PURPLE)
    c.drawString(20 * mm, A4[1] - 12 * mm, 'CURALLE Pilot RCT · PIS & Informed Consent')
    c.setFont('Sans', 8); c.setFillColor(MUTED)
    c.drawRightString(A4[0] - 20 * mm, A4[1] - 12 * mm, 'Protocol No. [__________] · Ethics Ref. [__________]')
    c.setStrokeColor(RULE); c.line(20 * mm, A4[1] - 14 * mm, A4[0] - 20 * mm, A4[1] - 14 * mm)
    c.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)
    c.drawString(20 * mm, 10.5 * mm, VERSION.replace('[', '').replace(']', ''))
    c.drawCentredString(A4[0] / 2, 10.5 * mm, 'Participant ID / ID Peserta: ________   Initials / Inisial: ______')
    c.drawRightString(A4[0] - 20 * mm, 10.5 * mm, f'Page / Muka surat {doc.page}')
    c.restoreState()

# ---------------------------------------------------------------- content
VISITS_EN = [
    ['Visit', 'When', 'What happens (about [60] minutes per visit)'],
    ['Visit 1<br/>Screening &amp; baseline', 'Week 0 (Day 1)',
     'Consent; check you are eligible; medical history and current medicines; skin examination; eczema scores (EASI, SCORAD); questionnaires (POEM, itch score, DLQI); skin water-loss (TEWL) and hydration readings; photographs of a treated area (optional); urine pregnancy test if relevant; random assignment; you receive the study cream, diary and instructions.'],
    ['Visit 2', 'Week [2] (± [3] days)',
     'Skin examination and eczema scores; questionnaires; TEWL and hydration; check of side effects, diary and cream use; resupply of cream.'],
    ['Visit 3', 'Week [4] (± [3] days)',
     'As Visit 2.'],
    ['Visit 4<br/>End of study', 'Week [6] (± [3] days)',
     'Final skin examination, scores, questionnaires, TEWL and hydration; photographs (optional); return of all cream tubes and diary; product acceptability questions; end-of-study check.'],
]
VISITS_BM = [
    ['Lawatan', 'Bila', 'Apa yang dilakukan (lebih kurang [60] minit setiap lawatan)'],
    ['Lawatan 1<br/>Saringan &amp; asas', 'Minggu 0 (Hari 1)',
     'Keizinan; semakan kelayakan; sejarah perubatan dan ubat semasa; pemeriksaan kulit; skor ekzema (EASI, SCORAD); soal selidik (POEM, skor gatal, DLQI); bacaan kehilangan air kulit (TEWL) dan kelembapan; gambar kawasan yang dirawat (pilihan); ujian kehamilan air kencing jika berkaitan; pembahagian rawak; anda menerima krim kajian, diari dan arahan.'],
    ['Lawatan 2', 'Minggu [2] (± [3] hari)',
     'Pemeriksaan kulit dan skor ekzema; soal selidik; TEWL dan kelembapan; semakan kesan sampingan, diari dan penggunaan krim; bekalan krim baharu.'],
    ['Lawatan 3', 'Minggu [4] (± [3] hari)', 'Sama seperti Lawatan 2.'],
    ['Lawatan 4<br/>Akhir kajian', 'Minggu [6] (± [3] hari)',
     'Pemeriksaan kulit akhir, skor, soal selidik, TEWL dan kelembapan; gambar (pilihan); pemulangan semua tiub krim dan diari; soalan penerimaan produk; semakan akhir kajian.'],
]

def pis_en():
    s = [P('PARTICIPANT INFORMATION SHEET', 'title'), P(TITLE_EN, 'sub')]
    s += [table([['Principal Investigator', '[Name, qualifications], [Department], Universiti Teknologi MARA (UiTM)'],
                 ['Co-investigators', '[Names]'],
                 ['Study site(s)', '[Clinic / hospital name and address]'],
                 ['Sponsor / funder', '[Funder name and grant number]'],
                 ['Registration', 'NMRR ID: [__________] · Clinical trial registry: [__________]']],
                [42 * mm, W - 42 * mm], header=False, shade_first_col=True), Spacer(1, 6)]
    s += [H('1. Introduction'),
          P('You are invited to take part in a research study. Before you decide, it is important that you understand why the study is being done and what it will involve. Please read this information carefully and discuss it with family, friends or your doctor if you wish. Ask the study team if anything is unclear or if you would like more information. Take your time to decide.'),
          H('2. What is the purpose of this study?'),
          P('Atopic dermatitis (eczema) is a long-term skin condition linked to a weak skin barrier, inflammation and an imbalance of the bacteria that live on the skin. Current treatments mainly control symptoms. CURALLE is a cream containing <b>postbiotics</b> (substances produced by beneficial bacteria, <b>not live bacteria</b>) carried in <b>glycerosomes</b> (tiny glycerol-based vesicles that help ingredients enter the skin without alcohol). It is made with a Halal-compliant, plant-based process.'),
          P('This is a <b>pilot study</b>. Its purpose is to find out whether CURALLE is safe and well tolerated, whether a larger study is practical, and to get a first estimate of how well it improves eczema compared with a <b>vehicle cream</b> (the same cream base without the postbiotic active ingredient). About <b>[60]</b> adults will take part at [number] site(s).'),
          H('3. Why have I been invited?'),
          P('You have been invited because you are aged 18 years or older and have mild-to-moderate atopic dermatitis. The study doctor will confirm whether you are eligible at the first visit. You may <b>not</b> be able to take part if, for example, you are pregnant or breastfeeding, have infected eczema, use oral or injected treatments for eczema, have a known allergy to any of the cream’s ingredients, or are taking part in another study. [Add or edit criteria to match the approved protocol.]'),
          H('4. Do I have to take part?'),
          P('No. Taking part is entirely <b>voluntary</b>. If you decide not to take part, or to stop at any time without giving a reason, this will <b>not</b> affect your standard medical care or your relationship with your doctors.'),
          H('5. What will happen if I take part?'),
          P('You will be in the study for about <b>[6] weeks</b> and will attend <b>4 visits</b> at [site]. A computer will assign you <b>by chance</b> (like tossing a coin) to one of two groups: CURALLE cream or vehicle cream. You have an equal (1 in 2) chance of being in either group. The study is <b>double-blind</b>: neither you nor the study team will know which cream you are using. In an emergency, the study doctor can find out quickly.')]
    s += [Spacer(1, 3), table(VISITS_EN, [30 * mm, 30 * mm, W - 60 * mm]), Spacer(1, 4)]
    s += [P('All skin measurements are <b>non-invasive</b>: a small probe rests on the skin surface for a few seconds. There are <b>no injections and no blood tests</b> in this study. [Edit if the protocol differs.]'),
          H('6. What will I be asked to do?'),
          *UL(['Apply a thin layer of the study cream to the affected areas <b>twice a day</b> (morning and night) on clean, dry skin, as shown by the study team.',
               'Do not use other creams, ointments or medicines on your eczema unless the study doctor allows it. [State the allowed bland emollient and any rescue treatment.]',
               'Stop using topical steroids or calcineurin inhibitors for [2] weeks before Visit 1, if the study doctor advises it.',
               'Fill in the daily diary (cream use, itch, any side effects) and bring it, with all tubes (used and unused), to each visit.',
               'Tell the study team about any new medicines, illness, or changes to your skin.',
               'Women who could become pregnant should use effective contraception during the study and tell the study team immediately if they become pregnant.']),
          H('7. What are the possible side effects, risks and discomforts?'),
          P('CURALLE has shown good safety in laboratory and pre-clinical testing and in skin-compatibility testing in healthy volunteers [update when available]. As with any cream, possible side effects include:'),
          *UL(['mild stinging, burning, itching, redness or dryness where the cream is applied;',
               'allergic contact reaction (rare): rash, swelling or blistering. Stop using the cream and contact the study team;',
               'your eczema may not improve, or may get worse, particularly if you are in the vehicle group. The study doctor will monitor you and can start standard treatment if needed;',
               'unknown risks: because this is a new product, there may be side effects that are not yet known. You will be told of any new information that may affect your decision to continue.']),
          P('Visits take time and you may need to travel. Photographs are taken only with your separate permission, and of the skin area only; your face will not be photographed unless the affected area is on the face [edit as needed].'),
          H('8. What are the possible benefits?'),
          P('Your eczema may improve, but this cannot be guaranteed. You will have regular skin assessments by the study team. The information from this study may help develop better, safer treatments for people with eczema in the future.'),
          H('9. Will I be paid? Are there any costs?'),
          P('You will receive an honorarium of <b>RM50 for each completed visit</b> (up to <b>RM200</b> for all 4 visits) as a token of appreciation for your time and travel. It will be paid [in cash / by bank transfer] at the end of each visit [or within [14] days], and you will sign a receipt. If you stop early, you keep the payment for all visits you have completed. The study cream, assessments and study-related tests are provided <b>free of charge</b>.'),
          H('10. What if something goes wrong?'),
          P('If you have a side effect or injury that you believe is caused by the study, contact the study team immediately on the number below. You will receive appropriate medical treatment. The study is covered by clinical trial insurance [Insurer, policy no. ______] for injury caused by taking part, in line with the Malaysian Guideline for Good Clinical Practice. Signing this form does not take away any of your legal rights.'),
          H('11. What happens if I stop taking part?'),
          P('You may withdraw at any time. We may ask you to attend a final safety check and return any unused cream. Information collected up to the time you withdraw may still be used, unless you ask us in writing not to use it, where this is possible. The study doctor may also stop your participation if it is in your best interest, if you do not follow study instructions, or if the study is stopped by the sponsor or ethics committee.'),
          H('12. Will my information be kept confidential?'),
          P('Yes. Your records will be identified only by a <b>study code</b>, not your name. Information is handled under the <b>Personal Data Protection Act 2010</b> and the Malaysian Guideline for Good Clinical Practice. Your records may be looked at by the study team, the Research Ethics Committee, the regulatory authority (NPRA) and authorised monitors or auditors, only to check that the study is done properly. Study records will be kept securely for at least [7] years after the study ends. You will not be identified in any report or publication.'),
          H('13. What will happen to the results?'),
          P('The results will be published in scientific journals and presented at meetings without identifying you, and will be used to plan a larger trial and support product registration. You may ask the study team for a summary of the results when the study is completed.'),
          H('14. Who has reviewed this study?'),
          P('This study has been reviewed and approved by the [Research Ethics Committee, Universiti Teknologi MARA / Medical Research &amp; Ethics Committee, Ministry of Health Malaysia] (Ref: [__________]).'),
          H('15. Who can I contact?'),
          table([['For questions about the study, side effects or injury', '[PI name], [phone], [email]<br/>After hours / emergency: [24-hour number]'],
                 ['For questions about your rights as a participant', 'Secretariat, [Ethics Committee name], [address], Tel: [__________], Email: [__________]']],
                [62 * mm, W - 62 * mm], header=False, shade_first_col=True),
          Spacer(1, 6),
          P('You will be given a copy of this information sheet and your signed consent form to keep.', 'small')]
    return s

def icf_en():
    s = [P('INFORMED CONSENT FORM', 'title'), P(TITLE_EN, 'sub'),
         P('Please <b>initial each box</b> to show you agree. Do not sign if you have any questions that have not been answered.'),
         tick_rows([
             'I confirm that I have read (or had read to me) and understood the Participant Information Sheet, Version [1.0] dated [dd/mm/yyyy], for the above study.',
             'I have had the opportunity to consider the information and ask questions, and my questions have been answered satisfactorily.',
             'I understand that my participation is voluntary and that I am free to withdraw at any time, without giving a reason and without my medical care or legal rights being affected.',
             'I understand that I will be randomly assigned to CURALLE cream or a vehicle cream, and that neither I nor the study team will know which one I receive.',
             'I agree to attend 4 study visits and to follow the study instructions, including applying the cream twice daily and keeping the diary.',
             'I understand I will receive an honorarium of RM50 for each completed visit (maximum RM200), and that I keep the payment for visits completed if I withdraw.',
             'I understand that my study records may be looked at by authorised people from the study team, the Ethics Committee, the regulatory authority and the sponsor’s monitors/auditors, and I give permission for them to access my records.',
             'I agree to my coded data being used for this study and in publications in which I cannot be identified, in line with the Personal Data Protection Act 2010.',
             'I agree to my general practitioner / treating doctor being informed of my participation. (Optional: initial only if you agree.)',
             'I agree to take part in the above study.']), PageBreak(),
         H('Optional: photographs of the treated skin area'),
         table([['I agree to photographs of my skin being taken for study assessment only.', 'YES ☐   NO ☐'],
                ['I agree that de-identified photographs may be used in scientific publications or presentations.', 'YES ☐   NO ☐'],
                ['I agree to be contacted about future related studies.', 'YES ☐   NO ☐']],
               [W - 34 * mm, 34 * mm], header=False), Spacer(1, 10)]
    s += sig_block(['Participant'])
    s += [P('<b>Impartial witness</b> (required only if the participant cannot read; the witness confirms that the information was read out accurately and that consent was given freely).', 'small')]
    s += sig_block(['Impartial witness'])
    s += [P('<b>Person obtaining consent</b>: I have explained the study to the participant and believe they understood and freely agreed to take part.', 'small')]
    s += sig_block(['Person obtaining consent (Investigator)'])
    s += [P('Copies: 1 for the participant · 1 for the Investigator Site File · 1 for the medical record.', 'small')]
    return s

def pis_bm():
    s = [P('RISALAH MAKLUMAT PESERTA', 'title'), P(TITLE_BM, 'sub')]
    s += [table([['Penyelidik Utama', '[Nama, kelayakan], [Jabatan], Universiti Teknologi MARA (UiTM)'],
                 ['Penyelidik bersama', '[Nama-nama]'],
                 ['Lokasi kajian', '[Nama dan alamat klinik / hospital]'],
                 ['Penaja / pembiaya', '[Nama pembiaya dan nombor geran]'],
                 ['Pendaftaran', 'ID NMRR: [__________] · Pendaftaran ujian klinikal: [__________]']],
                [42 * mm, W - 42 * mm], header=False, shade_first_col=True), Spacer(1, 6)]
    s += [H('1. Pengenalan'),
          P('Anda dijemput untuk menyertai satu kajian penyelidikan. Sebelum membuat keputusan, adalah penting untuk anda memahami mengapa kajian ini dijalankan dan apa yang terlibat. Sila baca maklumat ini dengan teliti dan bincangkan dengan keluarga, rakan atau doktor anda jika mahu. Tanya pasukan kajian jika ada perkara yang kurang jelas. Ambil masa anda untuk membuat keputusan.'),
          H('2. Apakah tujuan kajian ini?'),
          P('Dermatitis atopik (ekzema) ialah penyakit kulit jangka panjang yang berkait dengan lapisan pelindung kulit yang lemah, keradangan dan ketidakseimbangan bakteria pada kulit. Rawatan semasa kebanyakannya hanya mengawal simptom. CURALLE ialah krim yang mengandungi <b>postbiotik</b> (bahan yang dihasilkan oleh bakteria baik, <b>bukan bakteria hidup</b>) yang dibawa dalam <b>glycerosome</b> (vesikel kecil berasaskan gliserol yang membantu bahan menembusi kulit tanpa alkohol). Ia dihasilkan melalui proses berasaskan tumbuhan yang patuh Halal.'),
          P('Ini ialah <b>kajian rintis</b>. Tujuannya adalah untuk mengetahui sama ada CURALLE selamat dan boleh diterima, sama ada kajian yang lebih besar boleh dilaksanakan, dan untuk mendapatkan anggaran awal keberkesanannya berbanding <b>krim vehikel</b> (asas krim yang sama tanpa bahan aktif postbiotik). Kira-kira <b>[60]</b> orang dewasa akan menyertai kajian di [bilangan] lokasi.'),
          H('3. Mengapa saya dijemput?'),
          P('Anda dijemput kerana anda berumur 18 tahun ke atas dan menghidap dermatitis atopik ringan hingga sederhana. Doktor kajian akan mengesahkan kelayakan anda pada lawatan pertama. Anda mungkin <b>tidak</b> layak jika, sebagai contoh, anda hamil atau menyusu, mempunyai ekzema yang dijangkiti, menggunakan rawatan ekzema secara oral atau suntikan, alah kepada mana-mana bahan dalam krim, atau sedang menyertai kajian lain. [Tambah atau ubah kriteria mengikut protokol yang diluluskan.]'),
          H('4. Adakah saya wajib menyertai kajian ini?'),
          P('Tidak. Penyertaan adalah <b>sukarela</b> sepenuhnya. Jika anda memilih untuk tidak menyertai, atau berhenti pada bila-bila masa tanpa memberi sebab, keputusan ini <b>tidak</b> akan menjejaskan rawatan perubatan biasa anda atau hubungan anda dengan doktor.'),
          H('5. Apa yang akan berlaku jika saya menyertai kajian ini?'),
          P('Anda akan berada dalam kajian selama kira-kira <b>[6] minggu</b> dan menghadiri <b>4 lawatan</b> di [lokasi]. Komputer akan menempatkan anda <b>secara rawak</b> (seperti membaling syiling) ke dalam salah satu daripada dua kumpulan: krim CURALLE atau krim vehikel. Peluang anda berada dalam mana-mana kumpulan adalah sama (1 dalam 2). Kajian ini adalah <b>dua-buta</b>: anda dan pasukan kajian tidak akan tahu krim yang anda gunakan. Dalam kecemasan, doktor kajian boleh mengetahuinya dengan segera.')]
    s += [Spacer(1, 3), table(VISITS_BM, [30 * mm, 30 * mm, W - 60 * mm]), Spacer(1, 4)]
    s += [P('Semua pengukuran kulit adalah <b>tidak invasif</b>: alat kecil diletakkan pada permukaan kulit selama beberapa saat. <b>Tiada suntikan dan tiada ujian darah</b> dalam kajian ini. [Ubah jika protokol berbeza.]'),
          H('6. Apa yang perlu saya lakukan?'),
          *UL(['Sapukan lapisan nipis krim kajian pada kawasan yang terjejas <b>dua kali sehari</b> (pagi dan malam) pada kulit yang bersih dan kering, seperti yang ditunjukkan oleh pasukan kajian.',
               'Jangan gunakan krim, salap atau ubat lain pada ekzema anda kecuali dibenarkan oleh doktor kajian. [Nyatakan pelembap biasa yang dibenarkan dan rawatan penyelamat.]',
               'Berhenti menggunakan steroid topikal atau perencat kalsineurin selama [2] minggu sebelum Lawatan 1, jika dinasihatkan oleh doktor kajian.',
               'Isi diari harian (penggunaan krim, gatal, kesan sampingan) dan bawa bersama semua tiub (yang telah dan belum digunakan) pada setiap lawatan.',
               'Maklumkan pasukan kajian tentang sebarang ubat baharu, penyakit atau perubahan pada kulit anda.',
               'Wanita yang boleh hamil perlu menggunakan kaedah perancang keluarga yang berkesan semasa kajian dan segera memaklumkan pasukan kajian jika hamil.']),
          H('7. Apakah kesan sampingan, risiko dan ketidakselesaan yang mungkin berlaku?'),
          P('CURALLE telah menunjukkan tahap keselamatan yang baik dalam ujian makmal, praklinikal dan ujian keserasian kulit pada sukarelawan sihat [kemas kini apabila ada]. Seperti krim lain, kesan sampingan yang mungkin berlaku termasuk:'),
          *UL(['rasa pedih, panas, gatal, kemerahan atau kering di tempat krim disapu;',
               'tindak balas alahan (jarang berlaku): ruam, bengkak atau melepuh. Berhenti menggunakan krim dan hubungi pasukan kajian;',
               'ekzema anda mungkin tidak bertambah baik atau menjadi lebih teruk, terutamanya jika anda dalam kumpulan vehikel. Doktor kajian akan memantau anda dan boleh memulakan rawatan biasa jika perlu;',
               'risiko yang belum diketahui: kerana ini produk baharu, mungkin ada kesan sampingan yang belum diketahui. Anda akan dimaklumkan tentang sebarang maklumat baharu yang boleh menjejaskan keputusan anda untuk meneruskan.']),
          P('Lawatan mengambil masa dan anda mungkin perlu bergerak ke lokasi kajian. Gambar hanya diambil dengan kebenaran berasingan anda, dan hanya bahagian kulit yang terlibat; wajah anda tidak akan diambil gambar kecuali kawasan terjejas berada di muka [ubah jika perlu].'),
          H('8. Apakah faedah yang mungkin diperoleh?'),
          P('Ekzema anda mungkin bertambah baik, tetapi ini tidak dapat dijamin. Anda akan menerima penilaian kulit secara berkala oleh pasukan kajian. Maklumat daripada kajian ini boleh membantu menghasilkan rawatan yang lebih baik dan selamat untuk pesakit ekzema pada masa hadapan.'),
          H('9. Adakah saya akan dibayar? Adakah sebarang kos?'),
          P('Anda akan menerima saguhati sebanyak <b>RM50 bagi setiap lawatan yang lengkap</b> (sehingga <b>RM200</b> untuk keempat-empat lawatan) sebagai tanda penghargaan atas masa dan perjalanan anda. Ia akan dibayar [secara tunai / pindahan bank] pada akhir setiap lawatan [atau dalam tempoh [14] hari], dan anda akan menandatangani resit. Jika anda berhenti awal, anda tetap menerima bayaran bagi semua lawatan yang telah lengkap. Krim kajian, penilaian dan ujian berkaitan kajian disediakan <b>secara percuma</b>.'),
          H('10. Bagaimana jika berlaku sesuatu yang tidak diingini?'),
          P('Jika anda mengalami kesan sampingan atau kecederaan yang anda percaya disebabkan oleh kajian ini, hubungi pasukan kajian dengan segera melalui nombor di bawah. Anda akan menerima rawatan perubatan yang sewajarnya. Kajian ini dilindungi oleh insurans ujian klinikal [Syarikat insurans, no. polisi ______] bagi kecederaan akibat penyertaan, selaras dengan Garis Panduan Amalan Klinikal Baik Malaysia. Menandatangani borang ini tidak menghilangkan sebarang hak undang-undang anda.'),
          H('11. Apa yang berlaku jika saya berhenti?'),
          P('Anda boleh menarik diri pada bila-bila masa. Kami mungkin meminta anda menghadiri semakan keselamatan terakhir dan memulangkan krim yang belum digunakan. Maklumat yang dikumpul sehingga anda menarik diri masih boleh digunakan, kecuali anda meminta secara bertulis supaya tidak digunakan, jika ia boleh dilakukan. Doktor kajian juga boleh menghentikan penyertaan anda jika ia untuk kebaikan anda, jika arahan kajian tidak dipatuhi, atau jika kajian dihentikan oleh penaja atau jawatankuasa etika.'),
          H('12. Adakah maklumat saya dirahsiakan?'),
          P('Ya. Rekod anda hanya dikenal pasti melalui <b>kod kajian</b>, bukan nama anda. Maklumat dikendalikan di bawah <b>Akta Perlindungan Data Peribadi 2010</b> dan Garis Panduan Amalan Klinikal Baik Malaysia. Rekod anda mungkin disemak oleh pasukan kajian, Jawatankuasa Etika Penyelidikan, pihak berkuasa kawal selia (NPRA) dan pemantau atau juruaudit yang diberi kuasa, hanya untuk memastikan kajian dijalankan dengan betul. Rekod kajian akan disimpan dengan selamat sekurang-kurangnya [7] tahun selepas kajian tamat. Anda tidak akan dikenal pasti dalam sebarang laporan atau penerbitan.'),
          H('13. Apa yang akan berlaku kepada hasil kajian?'),
          P('Hasil kajian akan diterbitkan dalam jurnal saintifik dan dibentangkan di persidangan tanpa mengenal pasti anda, dan akan digunakan untuk merancang kajian yang lebih besar serta menyokong pendaftaran produk. Anda boleh meminta ringkasan hasil kajian daripada pasukan kajian apabila kajian selesai.'),
          H('14. Siapa yang telah menyemak kajian ini?'),
          P('Kajian ini telah disemak dan diluluskan oleh [Jawatankuasa Etika Penyelidikan, Universiti Teknologi MARA / Jawatankuasa Etika &amp; Penyelidikan Perubatan, Kementerian Kesihatan Malaysia] (Ruj: [__________]).'),
          H('15. Siapa yang boleh saya hubungi?'),
          table([['Pertanyaan tentang kajian, kesan sampingan atau kecederaan', '[Nama Penyelidik Utama], [telefon], [e-mel]<br/>Selepas waktu pejabat / kecemasan: [nombor 24 jam]'],
                 ['Pertanyaan tentang hak anda sebagai peserta', 'Urus Setia, [Nama Jawatankuasa Etika], [alamat], Tel: [__________], E-mel: [__________]']],
                [62 * mm, W - 62 * mm], header=False, shade_first_col=True),
          Spacer(1, 6),
          P('Anda akan diberikan salinan risalah maklumat ini dan borang keizinan yang telah ditandatangani untuk simpanan anda.', 'small')]
    return s

def icf_bm():
    s = [P('BORANG KEIZINAN PESERTA', 'title'), P(TITLE_BM, 'sub'),
         P('Sila <b>tandatangan ringkas (inisial) dalam setiap kotak</b> untuk menunjukkan persetujuan anda. Jangan tandatangan jika masih ada soalan yang belum dijawab.'),
         tick_rows([
             'Saya mengesahkan bahawa saya telah membaca (atau dibacakan) dan memahami Risalah Maklumat Peserta, Versi [1.0] bertarikh [dd/mm/yyyy], bagi kajian di atas.',
             'Saya telah diberi peluang untuk menimbang maklumat dan bertanya soalan, dan soalan saya telah dijawab dengan memuaskan.',
             'Saya faham bahawa penyertaan saya adalah sukarela dan saya bebas menarik diri pada bila-bila masa, tanpa memberi sebab dan tanpa menjejaskan rawatan perubatan atau hak undang-undang saya.',
             'Saya faham bahawa saya akan ditempatkan secara rawak untuk menerima krim CURALLE atau krim vehikel, dan saya serta pasukan kajian tidak akan tahu krim yang saya terima.',
             'Saya bersetuju untuk menghadiri 4 lawatan kajian dan mematuhi arahan kajian, termasuk menyapu krim dua kali sehari dan mengisi diari.',
             'Saya faham bahawa saya akan menerima saguhati RM50 bagi setiap lawatan yang lengkap (maksimum RM200), dan saya tetap menerima bayaran bagi lawatan yang telah lengkap jika saya menarik diri.',
             'Saya faham bahawa rekod kajian saya mungkin disemak oleh pihak yang diberi kuasa daripada pasukan kajian, Jawatankuasa Etika, pihak berkuasa kawal selia dan pemantau/juruaudit penaja, dan saya memberi kebenaran untuk mereka mengakses rekod saya.',
             'Saya bersetuju data berkod saya digunakan untuk kajian ini dan dalam penerbitan yang tidak mengenal pasti saya, selaras dengan Akta Perlindungan Data Peribadi 2010.',
             'Saya bersetuju doktor am / doktor yang merawat saya dimaklumkan tentang penyertaan saya. (Pilihan: inisial hanya jika bersetuju.)',
             'Saya bersetuju untuk menyertai kajian di atas.'], initials='Inisial'), PageBreak(),
         H('Pilihan: gambar kawasan kulit yang dirawat'),
         table([['Saya bersetuju gambar kulit saya diambil untuk penilaian kajian sahaja.', 'YA ☐   TIDAK ☐'],
                ['Saya bersetuju gambar tanpa identiti digunakan dalam penerbitan atau pembentangan saintifik.', 'YA ☐   TIDAK ☐'],
                ['Saya bersetuju untuk dihubungi mengenai kajian berkaitan pada masa hadapan.', 'YA ☐   TIDAK ☐']],
               [W - 34 * mm, 34 * mm], header=False), Spacer(1, 10)]
    s += sig_block(['Peserta'], 'bm')
    s += [P('<b>Saksi tidak berkepentingan</b> (diperlukan hanya jika peserta tidak boleh membaca; saksi mengesahkan bahawa maklumat telah dibacakan dengan tepat dan keizinan diberi secara sukarela).', 'small')]
    s += sig_block(['Saksi tidak berkepentingan'], 'bm')
    s += [P('<b>Individu yang mendapatkan keizinan</b>: Saya telah menerangkan kajian ini kepada peserta dan percaya peserta memahami serta bersetuju secara sukarela untuk menyertainya.', 'small')]
    s += sig_block(['Individu yang mendapatkan keizinan (Penyelidik)'], 'bm')
    s += [P('Salinan: 1 untuk peserta · 1 untuk Fail Tapak Penyelidik · 1 untuk rekod perubatan.', 'small')]
    return s

def honorarium():
    s = [P('HONORARIUM ACKNOWLEDGEMENT / PENGAKUAN PENERIMAAN SAGUHATI', 'title'),
         P('RM50 per completed visit (maximum RM200) · RM50 bagi setiap lawatan yang lengkap (maksimum RM200)', 'sub'),
         table([['Participant name / Nama peserta', ''], ['Participant ID / ID peserta', ''],
                ['NRIC / No. K/P', ''], ['Payment method / Kaedah bayaran', 'Cash / Tunai ☐    Bank transfer / Pindahan bank ☐   Bank: ____________  Acc. No.: ________________']],
               [58 * mm, W - 58 * mm], header=False, shade_first_col=True), Spacer(1, 10),
         P('I acknowledge receipt of the honorarium below for my participation in the above study. / Saya mengaku telah menerima saguhati di bawah bagi penyertaan saya dalam kajian di atas.')]
    rows = [['Visit / Lawatan', 'Date / Tarikh', 'Amount / Jumlah', 'Participant signature / Tandatangan peserta', 'Paid by (name, sign) / Dibayar oleh']]
    for v in ['1 · Week / Minggu 0', '2 · Week / Minggu [2]', '3 · Week / Minggu [4]', '4 · Week / Minggu [6]']:
        rows.append([v, '', 'RM50.00', '', ''])
    rows.append(['<b>Total / Jumlah</b>', '', '<b>RM________</b>', '', ''])
    t = table(rows, [36 * mm, 24 * mm, 24 * mm, 44 * mm, W - 128 * mm], row_heights=[None] + [34] * 5)
    s += [t, Spacer(1, 10),
          P('Honorarium is a token of appreciation for time and travel and is not a payment for any risk. It is paid only for visits attended. / Saguhati ialah tanda penghargaan atas masa dan perjalanan, bukan bayaran bagi sebarang risiko. Ia dibayar hanya bagi lawatan yang dihadiri.', 'small'),
          P('Verified by / Disahkan oleh (PI): ______________________   Date / Tarikh: ____________', 'p'),
          Spacer(1, 16)]
    return s

def withdrawal():
    s = [P('WITHDRAWAL OF CONSENT / PENARIKAN KEIZINAN', 'title'), P(TITLE_EN, 'sub'),
         P('I wish to withdraw from the above study. I understand that this will not affect my medical care. / Saya ingin menarik diri daripada kajian di atas. Saya faham bahawa ini tidak akan menjejaskan rawatan perubatan saya.'),
         P('<b>Please tick one or more / Sila tanda satu atau lebih:</b>'),
         table([['☐', 'I agree that information already collected may be used. / Saya bersetuju maklumat yang telah dikumpul boleh digunakan.'],
                ['☐', 'I do not want information already collected to be used, where this is possible. / Saya tidak mahu maklumat yang telah dikumpul digunakan, jika boleh.'],
                ['☐', 'I agree to attend a final safety check. / Saya bersetuju menghadiri semakan keselamatan terakhir.']],
               [12 * mm, W - 12 * mm], header=False),
         Spacer(1, 6),
         P('Reason (optional) / Sebab (pilihan): ____________________________________________________________', 'p'),
         Spacer(1, 6)]
    s += sig_block(['Participant / Peserta'])
    s += sig_block(['Investigator / Penyelidik'])
    return s

def build(out):
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm,
                          title='CURALLE Pilot RCT – Participant Information Sheet & Informed Consent Form',
                          author='[Principal Investigator]', subject='PIS/ICF, English & Bahasa Melayu')
    doc.addPageTemplates([PageTemplate(id='main', frames=[Frame(20 * mm, 18 * mm, W, A4[1] - 38 * mm, id='f')], onPage=on_page)])
    story = pis_en() + [PageBreak()] + icf_en() + [PageBreak()] + pis_bm() + [PageBreak()] + icf_bm() + \
            [PageBreak()] + honorarium() + [PageBreak()] + withdrawal()
    doc.build(story)

if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'CURALLE_RCT_PIS_ICF.pdf')
