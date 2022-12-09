<!DOCTYPE html>
<html>

<body>

    <?php
$balls = [1, 1, 1, 1, 1, 1, 2, 1, 1];
$price = 100;
rsort($balls); // melakukan sorting descending untuk menemukan bola terberat
$firstBall = $balls[0]; // variable awalnya tidak diisi, selanjutnya akan digunakan untuk menyimpan bola terberat
$timbang = 0; // penimbangan dimulai dari 0 bukan 1

//tidak dibutuhkan perulangan karena sudah jelas ketika ditemukan bola terberat melalui descending
//maka bola pertama terberat, sedang sisanya bola standar
//for ($i = 0; $i <= count($balls) - 1; $i++){
//	if ($i < count($balls) - 1) {
//    	$timbang++;
//    } else {
//    	break;
//    }
//}

echo "bola standar = ".$balls[1]."<br>";// bola standartnya ada di index 1 sampai 8
$timbang++; // penimbangan pertama
echo "bola lebih berat = ".$balls[0]."<br>"; // bola terberatnya ada di index pertama setelah sorting
$timbang++; //penimbangan kedua
echo "berat total = ".($balls[1]*8+$balls[0])."<br>";
echo "biaya total = ".$timbang *$price."<br>";
?>

</body>

</html>