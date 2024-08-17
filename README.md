# tas-kagit-makas_oyunu
## Taş, Kağıt ve Makas Oyun Kodunun Çalışma Prensibi
**🚀 Başlangıç** <br/>
•	Oyun ilk olarak `tas_kagit_makas_ÖZGE_KIR()` fonksiyonu ile başlar. Sonrasında oyunun kurallarını ve ne yapmanız gerektiğini anlatan birkaç mesaj ekrana gelir. <br/>

**🔄 Oyun Döngüsü** <br/> 
•	Oyun, bir `while` döngüsü içerisinde çalışır ve bu döngü, oyuncu veya bilgisayar 2 galibiyet elde edene kadar devam eder. <br/>
•	Oyun toplamda 3 tur oynanacak şekilde tasarlanmıştır. Her turda kullanıcı istediği seçeneği seçer `(taş 🪨, kağıt 📄, makas ✂️ ya da çıkış 🚪)`, bilgisayar ise `çıkış` seçeneği dışında rastgele bir seçeneği seçer. <br/>
•	Kullanıcı, herhangi bir turda `çıkış` yazarak oyundan çıkabilir ve ekrana `🙏 Oynadığın için teşekkürler.` mesajı gelir. <br/>
•	Eğer kullanıcı daha önce hiç tur oynamadıysa, çıkış yapıldığında oyuncuya `Hadi ama daha yeni başladık! Oynamak istediğinde geri gel.` mesajı gösterilir. <br/>
•	Kullanıcı bu seçenekler dışında bir seçenek seçerse ekranda `Seçtiğiniz seçenek uygun değil. Lütfen taş, kağıt, makas veya çıkış seçeneklerinden birini seçiniz!` yazısı belirir ve oyun kaldığı yerde devam eder. Bu mesaj tur sayısını etkiler fakat kullanıcının oynaması gereken 3 tur içine dahil edilmez. <br/>

**🥇 Tur Seçimi ve Karşılaştırma** <br/>
•	Kullanıcının seçimi ile bilgisayarın seçimi karşılaştırılır ve galip belirlenir. Eğer turu kullanıcı kazandıysa ekrana `🎉 İyi iş, bu turu sen kazandın!` yazdırılır fakat turu bilgisayar kazandıysa ekrana `🤖 Haha, bu turu ben kazandım!` yazdırılır. <br/>

**🎯 Oyunun Sonu** <br/>
•	Eğer oyuncu 2 tur kazanırsa oyun biter ve oyuncuya `🏆 Tebrikler, oyunu kazandınız!` şeklinde bir tebrik mesajı gösterilir. Aynı şekilde bilgisayar kazanırsa kullanıcıya `🤖 Maalesef, bilgisayar oyunu kazandı.` mesajı iletilir. <br/>
•	Oyun bitiminde hem kullanıcıya hem de bilgisayara tekrar oynamak isteyip istemediği sorulur. Eğer kullanıcı veya bilgisayar oyuna devam etmek istemezse, oyun sona erer.<br/>
