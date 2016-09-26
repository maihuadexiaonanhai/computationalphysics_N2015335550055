# -*- coding: utf-8 -*-
import os
import time
a1='sszhhzDDhzszhzzhhzssss====ss=+===+====ss=szzzzzzzDDDDhDhzzsD'
a2='s+zhhzhhzzsshhzhzhhsss====ss==sss====szszzhhhzzzzhzDDDDDzssD'
a3='=+zzhhhhzzhzhhhhzzzssssszsszz=szss====ssszhhhhhhzszDhDDhz==h'
a4='=+zzhhhzzhhhzzhhzssss+szsssss=sss=s+=s=sszzzhhhDhzhhhhhhs+=h'
a5='z+shzzzzzhzhhhzhsssss+=sszs=s=sssss=====szszhhzzhhsshhhhs(=h'
a6='s<=hhzzzhsszhhzsshhzs=+szzsss===ssss==+=szzszzzzzzhzhDhh=<hh'
a7='=<=hhzzzzszzss=szhhszs=+shssss==ssss=+<szzzszzhzszzzhDDh+=hh'
a8='+=shDshzzssz=sszzs=szz=+=zs=+s==s======zzzzzhzzhzsszshBh=<sh'
a9='<==szsszzsssszsss+++zz=++sz==s=====+=+=zssshzzzzszszszDh=<+h'
a10='(((<=s=sssssssss=+===s=<+=ssssss=s==++=ss+==ss=sszsss=+++<<z'
a11='((<+=sssssss=++=+<+++s+<====ssszs=s=+<=s==+++=sszz====<((((+'
a12='<<<+++=s=s===+++++++ss+++====sss====++zs=<++++=sss====+((<(('
a13='+((<<=s=+==s=s=+=(<=sh++==s==ss=====++sz=++==+<=ss=+<<<((((<'
a14='<((<+++=====++++++++szs=+=s=s=s=====+=zs++++=+<<=====<<((((<'
a15='(<+<<+=+=s=+<=szszs=sss=======s======sz=+=+=s+<<<==+++<((~~('
a16='<++<<+++=ssszDDhDBBDzsssss====+=+==ssss=zDDDDhs<<==+<<((((~('
a17='++<<<<<+=szshhsshz=hDs==ss==+=<<+=ss=+=hBDsshBD=<+++<(~((<(('
a18='=<++<+++=zs+hs+zDs--hh=+===+=+<<+=s=++hDh<.-=sh=+++<<(((~(<('
a19='+<=+=====+<<z=<hDhz=sDs<<+=++<(<++=<(zszh=~s+<s+<===<<(((((('
a20='++=+++<<(<(<z=<hBBNh=hD+<+=<<<(<<+<(+z+sDDDD<<z=~(+=+<(<(~(('
a21='+===+<<<<<<<ss<=hBD++hB<(<<<<<((<<~-sh<=BNNz<<z+~(<<<((<(((('
a22='==ss=++=+<<<=z+(+=+<=BB<(<<<<<(<(<~-zB<(=Dh+(sz(~~<<<((+<((('
a23='==ss=====+++<=z=+<+sDBB<~<<(<<((((-~zNz((+<(=h+~((<<<<(<<(<<'
a24='==========+<+<+szhhDDDD<-(<((((~~~~~zDDh=+=zh=((<+++<<(<<<<<'
a25='===s========+<<<++++<+D+~(<(((((~~~(s+=shzzs<(+=++++<((<(<<<'
a26='=====s=======++((~~~-+h=(<<<+<((((-(s<--(<<((<====+<<((<<<(+'
a27='==+===ss======+=<~((<+==((<<(~~(((-<=+~--~(<+++++=+<<(((<+<+'
a28='s=====ssss=+++==++++=<++(<+~~---((~++(((((<++++<+++<<((((<<='
a29='ss===sss=s==s=+=+++++<<+(<(~~~~-~(~<<~(<<<<=<<=+++<<<<((<<<='
a30='sss==sszssss=s=+++++<((<=<(~~~~--~<=<~~(<<<+<<+++<<+<<<(+<<s'
a31='sssssszzszss=====+++<((=s<(~~~~~~~+=(~(~(+<<++++++==++<<=<=s'
a32='ssssszhhzzzssss==++<<((+s+<(~~~~~(=+--~~~<<<++++===s++<+++zs'
a33='zssssszzzzzhzsss=++<<~(<+=<<((~(((=(--~(((<+++=szs=s=++++=zz'
a34='hsszzssszzzhzss=s++<((((+===<((<+<+~---~(<<<=sszsss====+=szz'
a35='hzsszzzsszzzhsszz=<<<<<<=szz=+==ss=<-~~(~(+=+=sss==s===+szzz'
a36='hhzsszzzzzzzzzzhzss=<+++shDhhzzhhhh(~(((<+=+=ssssszss===szzs'
a37='zhzssszzzzzzzhz=+=s+==+<<zDDDDhDDz<-~(<<+<((=ssszzzs===zzzss'
a38='hhhhzzzzzzzzzhz=ss=s++<<(<zBDDDDh<-~~(~(<<++====+===++szzsss'
a39='hhhhzzzzzzzzzzzssszzss==+<+hDDDD+~~(<+<+=+++szzzzzs==szzssss'
a40='zhhhhhhzzzzzzzzzss=======+++hBB=(<<<(<<++==szssszs=+=zhzzsss'
a41='zhhhDhhzzzsszzzhzsszzss+===+sDh+==+<<++===ssssssss=szhhzzzzs'
a42='hhhhhhhhzzzzhhhhhzsssss=ssssshzs=++=+=+==sssssss=sszhzzzzzzs'
a43='zzhhhhhhDDhhhhhhhzzzssssszsszhhz=======ssssszsss=shhhzzzsszs'
a44='zzzhzhhDDDDDhhhhhhhzzzzhhhzhhhhhzzzhzssszzzzzzszhzhhzzzzzzzs'
a45='zzzzhhhhDhDDDhhhDhhhhzzhhhhzzhzzhhhhzszzhzzszhhhhhhzzzzsszzs'
a46='zzzhhhhhDDDDDDDDDDDhhhzs=zzzzzzzss=szzhhhhhhhDDhhzzzzzzzzsss'
a47='zzzhhhhhDhhhDDDDDDDDDDhzzs=szss==szzhhDDDDDDDDhhhhzzzzzzzzsz'
a48='zzhhhhhhhhhhDDDDDDDDDDDDDzs=ss==szDDDDDDDDDDDhhDDhhzzzzzzzsz'
a49='zzhhzhhhhhhDDDDDDDDDDDDDDDhhhhzhDDDhDDDDDDhhhhhhhhhzzzzzzzsz'
a50='zzzzzhhhhhhhDDDDDDDDDDDDDDDDDDDDDDhDDDhhhhhhhzhzzzhzzzzzzzzs'
a51='sszhhzDDhzszhzzhhzssss====ss=+===+====ss=szzzzzzzDDDDhDhzzsD'
a52='s+zhhzhhzzsshhzhzhhsss====ss==sss====szszzhhhzzzzhzDDDDDzssD'
a53='=+zzhhhhzzhzhhhhzzzssssszsszz=szss====ssszhhhhhhzszDhDDhz==h'
a54='=+zzhhhzzhhhzzhhzssss+szsssss=sss=s+=s=sszzzhhhDhzhhhhhhs+=h'
a55='z+shzzzzzhzhhhzhsssss+=sszs=s=sssss=====szszhhzzhhsshhhhs(=h'
a56='=+zzhhhzzhhhzzhhzssss+szsssss=sss=s+=s=sszzzhhhDhzhhhhhhs+=h'
a57='z+shzzzzzhzhhhzhsssss+=sszs=s=sssss=====szszhhzzhhsshhhhs(=h'
a58='zzzhhhhhDhhhDDDDDDDDDDhzzs=szss==szzhhDDDDDDDDhhhhzzzzzzzzsz'
a59='zzhhhhhhhhhhDDDDDDDDDDDDDzs=ss==szDDDDDDDDDDDhhDDhhzzzzzzzsz'
a60='zzhhzhhhhhhDDDDDDDDDDDDDDDhhhhzhDDDhDDDDDDhhhhhhhhhzzzzzzzsz'
alphabet=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,\
a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,\
a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60]
os.system('cls')
for i in range(4):
    j=60-k
    k=j
    for j in range(59):
        for k in range(59):                   
        print alphabet[j][k]        
        print ''                         
    time.sleep(1)                       
    os.system('cls')




























