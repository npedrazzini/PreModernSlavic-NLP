import pandas as pd

df = pd.read_csv('/Users/nilo/Desktop/_TOROT_/stopwords.csv')
stopwordsdf = pd.DataFrame(df, columns=['lemma_id','pos','form','lemma'])

C = stopwordsdf[(stopwordsdf["pos"] == 'C-') & (stopwordsdf["lemma"] != 'FIXME')]
C = sorted(C["form"].unique())
print('C- =')
print("set(\n\"\"\"\n" + " ".join(C)+ "\n\"\"\".split()\n)")

Dq = stopwordsdf[(stopwordsdf["pos"] == 'Dq') & (stopwordsdf["lemma"] != 'FIXME')]
Dq = sorted(Dq["form"].unique())
print('Dq =')
print("set(\n\"\"\"\n" + " ".join(Dq)+ "\n\"\"\".split()\n)")

Du = stopwordsdf[(stopwordsdf["pos"] == 'Du') & (stopwordsdf["lemma"] != 'FIXME')]
Du = sorted(Du["form"].unique())
print('Du =')
print("set(\n\"\"\"\n" + " ".join(Du)+ "\n\"\"\".split()\n)")

G = stopwordsdf[(stopwordsdf["pos"] == 'G-') & (stopwordsdf["lemma"] != 'FIXME')]
G = sorted(G["form"].unique())
print('G- =')
print("set(\n\"\"\"\n" + " ".join(G)+ "\n\"\"\".split()\n)")

I = stopwordsdf[(stopwordsdf["pos"] == 'I-') & (stopwordsdf["lemma"] != 'FIXME')]
I = sorted(I["form"].unique())
print('I- =')
print("set(\n\"\"\"\n" + " ".join(I)+ "\n\"\"\".split()\n)")

Ma = stopwordsdf[(stopwordsdf["pos"] == 'Ma') & (stopwordsdf["lemma"] != 'FIXME')]
Ma = sorted(Ma["form"].unique())
print('Ma =')
print("set(\n\"\"\"\n" + " ".join(Ma)+ "\n\"\"\".split()\n)")

Pd = stopwordsdf[(stopwordsdf["pos"] == 'Pd') & (stopwordsdf["lemma"] != 'FIXME')]
Pd = sorted(Pd["form"].unique())
print('Pd =')
print("set(\n\"\"\"\n" + " ".join(Pd)+ "\n\"\"\".split()\n)")

Pi = stopwordsdf[(stopwordsdf["pos"] == 'Pi') & (stopwordsdf["lemma"] != 'FIXME')]
Pi = sorted(Pi["form"].unique())
print('Pi =')
print("set(\n\"\"\"\n" + " ".join(Pi)+ "\n\"\"\".split()\n)")

Pk = stopwordsdf[(stopwordsdf["pos"] == 'Pk') & (stopwordsdf["lemma"] != 'FIXME')]
Pk = sorted(Pk["form"].unique())
print('Pk =')
print("set(\n\"\"\"\n" + " ".join(Pk)+ "\n\"\"\".split()\n)")

Pp = stopwordsdf[(stopwordsdf["pos"] == 'Pp') & (stopwordsdf["lemma"] != 'FIXME')]
Pp = sorted(Pp["form"].unique())
print('Pp =')
print("set(\n\"\"\"\n" + " ".join(Pp)+ "\n\"\"\".split()\n)")

Pr = stopwordsdf[(stopwordsdf["pos"] == 'Pr') & (stopwordsdf["lemma"] != 'FIXME')]
Pr = sorted(Pr["form"].unique())
print('Pr =')
print("set(\n\"\"\"\n" + " ".join(Pr)+ "\n\"\"\".split()\n)")

Ps = stopwordsdf[(stopwordsdf["pos"] == 'Ps') & (stopwordsdf["lemma"] != 'FIXME')]
Ps = sorted(Ps["form"].unique())
print('Ps =')
print("set(\n\"\"\"\n" + " ".join(Ps)+ "\n\"\"\".split()\n)")

Pt = stopwordsdf[(stopwordsdf["pos"] == 'Pt') & (stopwordsdf["lemma"] != 'FIXME')]
Pt = sorted(Pt["form"].unique())
print('Pt =')
print("set(\n\"\"\"\n" + " ".join(Pt)+ "\n\"\"\".split()\n)")

Px = stopwordsdf[(stopwordsdf["pos"] == 'Px') & (stopwordsdf["lemma"] != 'FIXME')]
Px = sorted(Px["form"].unique())
print('Px =')
print("set(\n\"\"\"\n" + " ".join(Px)+ "\n\"\"\".split()\n)")

R = stopwordsdf[(stopwordsdf["pos"] == 'R-') & (stopwordsdf["lemma"] != 'FIXME')]
R = sorted(R["form"].unique())
print('R- =')
print("set(\n\"\"\"\n" + " ".join(R)+ "\n\"\"\".split()\n)")

V = stopwordsdf[(stopwordsdf["pos"] == 'V-') & (stopwordsdf["lemma"] != 'FIXME')]
V = sorted(V["form"].unique())
print('V- =')
print("set(\n\"\"\"\n" + " ".join(V)+ "\n\"\"\".split()\n)")