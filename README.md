Kelompok 13 :
1. Tengku Fredly Reinaldo (5025201198)
2. Ihsan Widagdo (5025211231)
3. Lihardo Marsoon Purba (5025211238)

Program ini dibuat dengan tujuan mempresentasikan iterasi terhadap titik ketiga yang dihitung dengan menggunakan metode bolzano demi mendapatkan akar suatu persamaan                                     polinomial.

Metode bolzano merupakan metode mencari akar persamaan dengan metode akolade dimana dibutuhkan iterasi demi mendapatkan nilai yang diinginkan dengan pendekatan di setiap iterasinya.

Penjelasan :
1. program ini membutuhkan suatu fungsi yang kita ingin cari akar - akarnya.\
![image](https://user-images.githubusercontent.com/95538168/198034154-ceb8c3aa-be2a-41f8-8468-fc6324691667.png)

2. metode ini menggunakan 2 titik x yang diketahui untuk pendekatan dan iterasinya, untuk itu kami meminta input dari user berupa data batas bawah dan batas atas.\
![image](https://user-images.githubusercontent.com/95538168/198035010-52d900c9-9b5c-498b-9052-fb2eaff8d555.png)

3. Untuk melakukan pendekatan yang semakin tepat dengan nilai benarnya, maka dilakukan beberapa iterasi. semakin banyak iterasi yang dilakukan maka nilai yang diperoleh    semakin tepat dengan nilai benarnya.
\
![image](https://user-images.githubusercontent.com/95538168/198036427-d20e3d56-45e3-4ce0-83c6-702f9706e8fd.png)

4. Bolzano menggunakan metode "nilai tengah" dimana mencari nilainya dengan menggunakan evaluasi nilai x demi mendapat nilai f(x) yang mendekati 0. Evaluasi nya            menggunakan fungsi yang telah di-inputkan ke dalam program. Mencari nilai evaluasi setiap x dimasukkan ke dalam variabel x3 dengan perhitungan x3 terletak di            pertengahan x1 dan x2.\
![image](https://user-images.githubusercontent.com/95538168/198038134-8c72cca7-600d-47d3-863d-51026b82fa0c.png)\
![image](https://user-images.githubusercontent.com/95538168/198038532-fe912700-68a3-437a-a45c-e4b0228006e5.png)

5. Setiap iterasinya terjadi pergantian x1 dan x2 yang ditukar dengan evaulasi x3 dari iterasi sebelumnya. pergantian titiknya ditentukan dengan nilai f(x) yang          didapat dari f(x3) dimana kita perlu mencari batas antara nilai f(x) yang positif dengan negatif dengan asumsi bahwa nilai 0 dari akar persamaan yang dicari            terlatak dari nilai f(x) yang berupa nilai postif dan negatif yang direpresentasikan dengan variabel x1 dan x2.\
![image](https://user-images.githubusercontent.com/95538168/198040532-b910f055-3f96-4233-a756-535ef02bd5fe.png)\
   perlu diperhatikan juga bahwa jika nilai f(x1) dan f(x2) menghasilkan nilai positif di keduanya atau negatif di keduanya maka iterasi selanjutnya tidak bisa            dilakukan, karena metode ini menggunakan pendekatan nilai f(x) postif dan negatif.\
   ![image](https://user-images.githubusercontent.com/95538168/198041228-53ee5c0e-aba9-4558-ad07-1ce8bb16fa34.png)
  
6. Hasil setiap iterasinya di print berupa tabel lengkap dengan iterasi yang telah dilakukan.\
![image](https://user-images.githubusercontent.com/95538168/198042313-621d16b6-6c25-4407-8f9e-bfe49bed1d0b.png)\
   dengan data yang diperoleh dari code di bawah ini dengan setiap perhitungan yang disimpan di variabel yang dievaluasi di setiap iterasinya.\
![image](https://user-images.githubusercontent.com/95538168/198043499-e76b8ec5-f44c-44ac-81b7-7b422fd8de80.png)\
   outputnya seperti di bawah ini :\
  ![image](https://user-images.githubusercontent.com/95538168/198042583-d19502ec-bb11-4501-b441-10bdc60a8a7b.png)
   


   



   






