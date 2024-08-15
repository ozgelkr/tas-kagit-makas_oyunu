import random

def tas_kagit_makas_ÖZGE_KIR():
    print('Dünyanın en ünlü oyunlarından birine hoş geldin!')
    print('Taş, kağıt, makas oynamaya hazır mısın?')
    print('Toplamda 3 tur oynayacağız ve bu turlardan 2 tanesini kazanan oyunu kazanır!')
    print('Oynamak için taş, kağıt ve makastan birini seç; eğer oynamak istemiyorsan çıkış yazman yeterli.')
    print('Hadi oyuna başlayalım!!!')

    oyun_sayaci = 0
    oyuncu_galibiyeti = 0
    pc_galibiyeti = 0
    en_az_bir_kez_oynandi = False

    while True:
        oyun_sayaci += 1
        tur_sayaci = 0
        oyuncu_galibiyeti = 0
        pc_galibiyeti = 0
        print('{}.Oyunumuz başlıyor!'.format(oyun_sayaci))
        print('Oyuncu Galibiyeti:', oyuncu_galibiyeti)
        print('Bilgisayar Galibiyeti:', pc_galibiyeti)

        while oyuncu_galibiyeti < 2 and pc_galibiyeti < 2:
            tur_sayaci += 1
            print('{}. Tur'.format(tur_sayaci))

            soru = input('Taş, kağıt, makas ya da çıkış: ').lower()
            kelimeler = ['taş', 'kağıt', 'makas']
            pc_secimi = random.choice(kelimeler)

            if soru == 'çıkış':
                if not en_az_bir_kez_oynandi:
                    print('Hadi ama daha yeni başladık! Oynamak istediğinde geri gel.')
                else:
                    print('Oynadığın için teşekkürler.')
                return

            if soru == 'taş':
                en_az_bir_kez_oynandi = True
                print('Bilgisyarın seçimi: ' + pc_secimi)
            elif soru == 'kağıt':
                en_az_bir_kez_oynandi = True
                print('Bilgisyarın seçimi: ' + pc_secimi)
            elif soru == 'makas':
                en_az_bir_kez_oynandi = True
                print('Bilgisyarın seçimi: ' + pc_secimi)
            else:
                print('Seçtiğiniz seçenek uygun değil. Lütfen taş, kağıt, makas veya çıkış seçeneklerinden birini seçiniz!')
                continue

            if soru == pc_secimi:
                print("Bu tur berabere!")
            elif (soru == 'taş' and pc_secimi == 'makas') or \
                    (soru == 'kağıt' and pc_secimi == 'taş') or \
                    (soru == 'makas' and pc_secimi == 'kağıt'):
                print("İyi iş, bu turu sen kazandın!")
                oyuncu_galibiyeti += 1
                print('Oyuncu Galibiyeti:', oyuncu_galibiyeti)
                print('Bilgisayarın Galibiyeti:', pc_galibiyeti)
            else:
                print("Haha, bu turu ben kazandım!")
                pc_galibiyeti += 1
                print('Oyuncu Galibiyeti:', oyuncu_galibiyeti)
                print('Bilgisayar Galibiyeti:', pc_galibiyeti)

        if oyuncu_galibiyeti == 2:
            print('Oyuncu Galibiyeti:', oyuncu_galibiyeti)
            print('Bilgisayar Galibiyeti:', pc_galibiyeti)
            print("Tebrikler, oyunu kazandınız!")
        else:
            print("Maalesef, bilgisayar oyunu kazandı.")
            print('{}.Turun Sonu - Oyuncu Galibiyeti: {}, Bilgisayar Galibiyeti: {}'.format(tur_sayaci, oyuncu_galibiyeti, pc_galibiyeti))

        oyuncu_devam = input('Tekrar oynamak ister misin? (evet/hayır): ').lower()
        pc_devam = random.choice(['evet', 'hayır'])
        print('Bilgisayar oyuna devam etmek istiyor mu?', pc_devam)

        if oyuncu_devam != 'evet' or pc_devam != 'evet':
            print("Oyun sona erdi. Tekrar görüşmek üzere!")
            break


tas_kagit_makas_ÖZGE_KIR()



