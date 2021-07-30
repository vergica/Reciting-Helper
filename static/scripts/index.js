$(document).ready(function() {
    $("#table").hide()
	var content = document.getElementById("table").innerHTML;
	document.getElementById("table").innerHTML = content.replace(RegExp("(" + $("#word").text() + ")", "ig"), "<font color=red>$1</font>");
    $("#source").attr("src", "http://dict.youdao.com/dictvoice?type=1&audio=" + $("#word").text())
});
var p = function() {
    myWindow=window.open("http://dict.youdao.com/dictvoice?type=1&audio=" + $("#word").text(),'','width=1,height=1');
    setTimeout(() =>myWindow.close(), 4000);
}
var ri = function() {
    number = document.cookie.match("number=(.*)")
    if(number == null){document.cookie="number=1"
    }else{
        document.cookie="number=" + String(Number(number[1]) + 1)
    }
    $("#alert").attr("class", "alert alert-success navbar-fixed-top");
    if(document.cookie.match("number=(.*)")[1] == 1){
        $("#alert").text("恭喜你，答对啦  ！*★,°*:.☆(￣▽￣)/$:*.°★* 。");
    }else{
        $("#alert").text("连对第" + document.cookie.match("number=(.*)")[1] + "个  ！*★,°*:.☆(￣▽￣)/$:*.°★* 。");
    }
    setTimeout(() =>window.location.reload(), 800)
}
var fa = function() {
    $("#alert").attr("class", "alert alert-warning navbar-fixed-top");
    $("#alert").text("貌似不对哦，再试一次吧  (☄⊙ω⊙)☄");
    document.cookie="number="
    $("#table").fadeIn(800)
}
