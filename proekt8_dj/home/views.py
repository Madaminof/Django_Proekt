
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse
# Create your views here.



def index(request):
    return HttpResponse("Salom, dunyo! Bu bizning birinchi view.")




def home(request):
    html_content = """
      <html>
    <head>
        <title>Salom</title>
        <style>
           
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
   background-color:rgb(225, 228, 235)
  }
  
  .logo{
      width: 50px;
      height:50px;
      border-radius: 25%;
      margin-left: 7px;
  }    
  .menu1{
      display: flex;
      background-color: rgb(66, 92, 124);
      border-radius: 10px;
      margin-left: 10px;
      padding: 10px;
      margin: 10px;
  
  }    
  .navv a:hover{
    color: aliceblue;
  }
  
  .navbar a {
      font-size: 14px;
      text-transform: uppercase;
      font-weight: 700;
      line-height: 50px;
      margin-left: 60px;
     transition: 0.5s;
     color: rgb(214, 214, 214);
     text-decoration: none;
  }
  .navbar a:hover,
  .navbar.menu1 {
      color: rgb(71, 71, 170);
  }
  
  h1{
      color: rgb(16, 17, 17);
      text-align: center;
      text-shadow: 2px 2px #bfc2c4;
  
  }
  
.box2{
    border: 1px solid black;
    height: 800px;
    display: flex;
    

}
.left{
    margin: 4px;
    border: 1px solid black;
    height: 750px;
    width: 30%;
    box-shadow: 1px 1px 5px rgb(43, 127, 229);

}
.left h1{
    text-align: center;
    margin-bottom: 10px;
    text-shadow: slategrey;
}
.right{
    margin: 4px;
    border: 1px solid black;
    height: 750px;
    width: 70%;
}

.item{
    border-bottom: 1px solid black;
    margin: 7px;
}
.item p a{
    text-decoration: none;
    color: black;
}
.item a:hover{
    text-decoration: none;
    color: rgb(255, 250, 250);
}
.item:hover{
    background-color: rgb(106, 158, 226);
}
.left1:hover{
    background-color: rgb(106, 158, 226);
    
    }
.center1 :hover{
    background-color: rgb(106, 158, 226);
    }
.right1:hover{
    background-color: rgb(106, 158, 226);    
   
    } 

.left1 p a:hover{
   color: aliceblue;

}  
 
  

  

.saber{
    display: flex;
    background-color: aliceblue;
    box-shadow: 1px 1px 5px rgb(43, 127, 229);
    width: 97%;


}
.saber img{
    margin: 10px;
    width: 30%;
    height: 200px;
    box-shadow: 1px 1px 5px rgb(43, 127, 229);

}
.saber div{
    width: 60%;
    height: 200px;
}
.saber div p a{
    color: black;
    text-decoration: none;
}

.box3{
    display: flex;
    margin: 15px;
    margin-bottom: 10px;
    text-align: center;
  
}
.pubg{
    width: 90%;
    margin: 10px;
    border-radius: 5px;
}
.clash{
    width: 90%;
    margin: 10px;
    border-radius: 5px;
    height: 128px;
}
.dota{
    width: 90%;
    margin: 10px;
    border-radius: 5px;
}
.left1{
    width: 35%;
    box-shadow: 1px 1px 5px rgb(43, 127, 229);

    margin-left: 10px;
}
.center1{
    width: 30%;
    box-shadow: 1px 1px 5px rgb(43, 127, 229);
    margin-left: 10px;
}
.right1{
    width: 30%;
    box-shadow: 1px 1px 5px rgb(43, 127, 229);
    margin-left: 10px;
}
.blur{
    width: 106%;
   
    margin-left: 10px;
}

.box2 div p a{
    color: black;
    text-decoration: none;
    text-align: center;
}

.blur img{
    margin: 7px;
    width: 30%;
    height: 150px;

}
.blur div{
    width: 90%;
    height: 165px;
}



.left p a:hover{
   color: aliceblue;
}

        </style>
    </head>
    <body>
        <div class="box">
        <div class="menu1">
            <img  class="logo" src="./image/kun.jpeg" alt="">
            <nav class="navbar">
                <a href="https://kun.uz/news/category/uzbekiston" class="active">O'ZBEKISTON</a>
                <a href="https://kun.uz/news/category/jahon">JAHON</a>
                <a href="https://kun.uz/news/category/iktisodiet">IQTISODIYOT</a>
                <a href="https://kun.uz/news/category/jamiyat">JAMIYAT</a>
                <a href="https://kun.uz/news/category/sport">SPORT</a>
                <a href="https://kun.uz/news/category/nuqtai-nazar">NUQTAI-NAZAR</a>
                <a href="https://kun.uz/news/audio/list">AUDIO</a>
                <a href="./contact.html">Contact</a>
            </nav>
           
        </div> 

    </div>
    <div class="box2">
        <div class="left">
            <div class="item">
                <h1>
                    Songgi Yangiliklar
                </h1>
                <p>
                    <a href="">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nobis dolor eum eveniet nam maiores dolores! Facilis perferendis harum non suscipit? Quia nihil itaque dolore ad veritatis eum, perspiciatis ipsa quidem laborum aliquam, eaque aperiam ex ullam est ipsum molestias officiis.
                    </a>
                </p>
            </div>
            <div class="item">
               
                <p>
                    <a href="">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nobis dolor eum eveniet nam maiores dolores! Facilis perferendis harum non suscipit? Quia nihil itaque dolore ad veritatis eum, perspiciatis ipsa quidem laborum aliquam, eaque aperiam ex ullam est ipsum molestias officiis.
                    </a>
                </p>
            </div>
            <div class="item">
               
                <p>
                    <a href="">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nobis dolor eum eveniet nam maiores dolores! Facilis perferendis harum non suscipit? Quia nihil itaque dolore ad veritatis eum, perspiciatis ipsa quidem laborum aliquam, eaque aperiam ex ullam est ipsum molestias officiis.
                    </a>
                </p>
            </div>
            <div class="item">
                <p>
                    <a href="">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nobis dolor eum eveniet nam maiores dolores! Facilis perferendis harum non suscipit? Quia nihil itaque dolore ad veritatis eum, perspiciatis ipsa quidem laborum aliquam, eaque aperiam ex ullam est ipsum molestias officiis.
                    </a>
                </p>
            </div>
            <div class="item">
               
                <p>
                    <a href="">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nobis dolor eum eveniet nam maiores dolores! Facilis perferendis harum non suscipit? Quia nihil itaque dolore ad veritatis eum, perspiciatis ipsa quidem laborum aliquam, eaque aperiam ex ullam est ipsum molestias officiis.
                    </a>
                </p>
            </div>
            <div class="item">
               
                <p>
                    <a href="">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nobis dolor eum eveniet nam maiores dolores! Facilis perferendis harum non suscipit? Quia nihil itaque dolore ad veritatis eum, perspiciatis ipsa quidem laborum aliquam, eaque aperiam ex ullam est ipsum molestias officiis.
                    </a>
                </p>
            </div>

        </div>
        <div class="right">
            <div class="saber">
                
                <img src="data:image/jpeg;base64,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" alt="">
                <div class="item">
                    <p>
                        <a href="">Onlayn oyinlar tarixi 1970-yillarda kommutatsiyalangan tarmoqlar davrida boshlangan[1]. Birinchi bunday oyinlar matnga asoslangan edi  xususan, MUD1[en], 1978-yilda yaratilgan. Dastlab, u faqat ichki tarmoqda mavjud edi, lekin 1980-yilda ARPANET ga ulandi[2]. Keyingi on yillikda tijorat oyinlari paydo bola boshladi; birinchisi Islands of Kesmai[en]  1984-yilda chiqarilgan rolli kompyuter oyini[2]. Grafikaga koproq ́ oyinlar ham yaratila boshlandi:
                        </a>
                    </p>
                </div>
            </div>
            <div class="box3">
                <div class="left1">
                    <img class="pubg" src="/image/pubg.jpeg" alt="">
                    <p><a href="https://www.pubgmobile.com/en-US/home.shtml">PUBG Mobile - bu Tencent Games bo'limi LightSpeed & Quantum Studio tomonidan ishlab chiqilgan bepul jangovar qirollik videoo'yini. Bu PUBG: Battlegrounds mobil o‘yiniga moslashtirilgan va mobil versiyasidir. Dastlab u Android va iOS uchun 2018-yil 19-martda global versiyasini chiqarilgan.
                    </a></p>

                
                        
                </div>
                <div class="center1">
                    <img class="clash" src="./image/clash.jpeg" alt="">
                    <p><a href="https://supercell.com/en/games/clashofclans/">Clash of Clans(klanlar toʻqnashuvi) — bu 2012-yilda Finlandiya oʻyin ishlab chiqaruvchisi Supercell tomonidan ishlab chiqilgan va nashr etilgan bepul mobil strategik video oʻyin. Oʻyin iOS platformalari uchun 2012-yil 2-avgustda va Android uchun Google Playda 2013-yil 7-oktabrda chiqarilgan.
                    </a></p>
                </div>
                <div class="right1">
                    <img class="dota" src="./image/dota.jpeg" alt="">
                    <nav class="navv">
                        <p><a href="https://store.steampowered.com/app/570/Dota_2/">Dota 2 — bu Valve korporatsiyasi tomonidan ishlab chiqarilgan MOBA (Multiplayer Online Battle Arena) janridagi oʻyin. Dota 2 DotAning davomi boʻlib, Warcraft III: Reign of Chaos va uning qoʻshimcha qismi Warcraft III: The Frozen Throne uchun maxsus xarita hisoblanadi.
                        </a></p>
                    </nav>
                   
                </div>
            </div>

            <div class="blur">
                <div class="saber">
                    <img class="blur" src="./image/a2.jpeg" alt="">
                    <div class="item1">
                        <p>
                            <a href="https://store.epicgames.com/en-US/">Blur (oʻzbekcha — „Xiralashish“) — bu Bizarre Creations tomonidan yaratilgan va Activision Blizzard tomonidan 2010-yil may oyida PlayStation 3 va Xbox 360 konsollari va Windows shaxsiy kompyuterlari uchun chiqarilgan arkada poyga videooʻyini. Videooʻyin — bu haqiqiy avtomashinalar va sahnalar, arkada uslubidagi boshqaruv va avtomobildan mashinaga jangga ega poyga oʻyini. Rossiyada Blur 1C-SoftKlab[2] tomonidan nashr etilgan: shaxsiy kompyuterda oʻyin butunlay rus tilida chiqarilgan, konsollar uchun versiyalar tarjima qilinmagan. Kompyuterda Blur raqamli tarqatish xizmatida ham tarqatildi Steam, lekin keyinchalik avtomobil litsenziyasining amal qilish muddati tugaganligi sababli u yerdan olib tashlandi.
                            </a>
                        </p>
                </div>
            </div>

               
    </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
