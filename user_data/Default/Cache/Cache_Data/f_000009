function getCookieRia2(_cookieName) {
	var currcookie = "";
	var arrCookie = document.cookie.split(";");
	var cookieValue = "";

	for (var i = 0; i < arrCookie.length; i++) {
		if (arrCookie[i].indexOf("cgv.cookie=") != -1)
			currcookie = arrCookie[i].replace("cgv.cookie=", "");
	}

	var cookieList = currcookie.split("&");
	for (i = 0; i < cookieList.length; i++) {
		if (cookieList[i].indexOf(_cookieName + "=") > -1) {
			if (cookieList[i].split("=")[0].replace(/\s/g, "") == _cookieName) {
				cookieValue = decodeURIComponent(cookieList[i].split("=")[1]);
				break;
			}
		}
	}

	return cookieValue;
}

function getNonCookieRia(_cookieName) {
	var currcookie = "";
	var arrCookie = document.cookie.split(";");
	var cookieValue = "";

	for (var i = 0; i < arrCookie.length; i++) {
		if (arrCookie[i].indexOf("cgv.cookie=") != -1)
			currcookie = arrCookie[i].replace("cgv.cookie=", "");
	}

	var cookieList = currcookie.split("&");
	for (i = 0; i < cookieList.length; i++) {
		if (cookieList[i].indexOf(_cookieName + "=") > -1) {
			if (cookieList[i].split("=")[0].replace(/\s/g, "") == _cookieName) {
				cookieValue = cookieList[i].split("=")[1];
				break;
			}
		}
	}

	return cookieValue;
}

function dimapp() {
	/* 110924 attach CSK
	레이어 팝업 사용시 마스크를 생성*/
	var $lywrap = $('.lyRiaWrap');
	//var width = $(document).width();
	var height = $(document).height();
	var width = window.screen.width;
	//var height = window.screen.height;

	$lywrap.find('.mask')
		.css({ 'width': '100%', 'height': '100%' })
		.fadeTo("fast", 0.8)
	.end();
	$lywrap.find('.mask')
		.css({ 'z-index': '50', 'position': 'fixed', 'left': '0', 'top': '0', 'background': '#000' })
	.end();

	$('.mini').show();
}

// 예매
function riaWrapClose() {
	var $lywrap = $('.lyRiaWrap');
	$lywrap.find('.mask').fadeOut('fast');
	// 111004 attach CSK RIA닫을때 아래 레이어 visible
	// hidden 소스는 silverlight_link.js 812행
	if ($('.top_player').length > 0) { $('.top_player').css({ "visibility": 'visible' }) }
	$('#TopBanner').css({ "visibility": 'visible' });

	if ($("#secu_num").text() != "1")
		$("#silver").show();

	$('.mini').hide();
}

function openMiniRia()
{
	chkClickLog('/mini예매');
	window.open('/mini/User/Login.aspx', '' , 'width=420,height=721,toolbar=no,scrollbars=yes');
}

function riaReserveClose(){

		// 이벤트 임시 설정
		var now = new Date();
		var _sdate = new Date(2013, 9, 17, 0, 0, 0);
		var _edate = new Date(2013, 10, 15, 23, 50, 0);

		if (now > _sdate && now < _edate) 
		{
			window.open("/popup/popup.aspx?idx=135", 'RiaEvent', "width=320,height=385,top=150,left=345,toolbar=no,scrollbars=no,status=0,top=0,left=0");
		}
}


//상영시간표에서 영화 팝업플래시 띄우기
function ShowMovieInfo(CGVCode) {
	popfix("/popup/p_movieinfo.aspx?CGVCode=" + CGVCode, 'movieinfo', 775, 420, 1);

}

//리아 포스터 클릭시 영화상세정보 팝업 보기
function movieInfoOpen(CGVCode) {
	popfix("/popup/p_movieinfo.aspx?CGVCode=" + CGVCode, 'movieinfo', 775, 420, 1);
}

//리아 예매정보 보기 링크
function FlashReserveMyCGV() {
	location.href = "/mycgv/diary/reserve/default.aspx";
}

// 리아 극장 주변 정보 보기 
function FlashReservePlayground(tcode) {
	location.href = "/theater/theater/default.aspx?theaterCode=" + tcode;
}

//FlashGiftCon
function FlashGiftCon() {
	location.href = "/Shopping/giftcon/shop_list.aspx";
}

// 비밀번호 찾기
function fnFindAccount() {
	location.href = "/user/login/findAccount.aspx";
}

//빠른예매( 상영시간표 에서 호출하는데 영화코드랑 극장코드값이 없다;;)
function FastTicketing() {
	writeRiaObject();
}

function FastTicketing_hide() {
	// 2011-11-11 Dbros Csk Attach
	// rel 값이 open 일때만 실행 된다
	if ($('.ad_top_area').attr('rel') == 'open') {
		$('.ad_top_area')
			.attr('rel', '')
			.delay(500).slideDown();
	}
	document.getElementById("ria_div").style.display = "none";
	document.getElementById("ria_div").innerHTML = "";
	riaWrapClose();
	$('#TopBanner').css({ "visibility": 'visible' });
	$('#ADSmallWrapper').css({ "visibility": 'visible' });
	$('#ADSmallWrapper2').css({ "visibility": 'visible' });
	$('#ADShowRWrapper').css({ "visibility": 'visible' });
}

function SimpleTicketing_hide() {
	FastTicketing_hide();
}


/******** 인코딩 하지 않은 쿠키값 가져오기 ********/

function getCookieNoDecode(_cookieName) {
	var currcookie = setCookieNodecode("cgv.cookie");

	var cookieList = currcookie.split("&");
	var cookieValue = "";
	for (i = 0; i < cookieList.length; i++) {
		if (cookieList[i].indexOf(_cookieName + "=") > -1) {
			if (cookieList[i].split("=")[0].replace(/\s/g, "") == _cookieName) {
				cookieValue = cookieList[i].split("=")[1];
				break;
			}
		}
	}

	return cookieValue;
}

function setCookieNodecode(name) {
	var nameOfCookie = name + "=";
	var x = 0;
	while (x <= document.cookie.length) {
		var y = (x + nameOfCookie.length);
		if (document.cookie.substring(x, y) == nameOfCookie) {
			if ((endOfCookie = document.cookie.indexOf(";", y)) == -1)
				endOfCookie = document.cookie.length;
			return document.cookie.substring(y, endOfCookie);
		}
		x = document.cookie.indexOf(" ", x) + 1;
		if (x == 0)
			break;
	}
	return "";
}


//회원가입
function FJoin() {
	location.href = "https://www.cgv.co.kr/user/join/agreement.aspx";
}

//로그아웃
function FLogout() {
	location.href = "/user/login/logout.aspx";
}



// 리아 로그인
function FLogin(id, pwd, returnURL) {

	userId = id;
	userPassword = pwd;

	if (returnURL != "n" && returnURL != "") {
		returnURL = "http://www.cgv.co.kr/default.aspx?ria=y";
	} else {
		returnURL = location.href;
	}

	if (userId == "") {
		alert("회원 ID를 확인하세요.");
		return false;
	}
	if (userPassword == "") {
		alert("회원 비밀번호를 확인하세요.");
		return false;
	}

	var keyObject = document.getElementById("loginform");

	if (keyObject) {

		document.loginform.method = "post";
		document.loginform.id.value = userId;
		document.loginform.password.value = userPassword;
		document.loginform.returnURL.value = returnURL;
		document.loginform.action = "https://www.cgv.co.kr/user/login/flogin.aspx";
		document.loginform.submit();
	}
	else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}
}


function FIpin() {
	var keyObject = document.getElementById("loginform");

	if (keyObject) {
		location.href = "https://www.cgv.co.kr/user/ipin/Ipin_Common.aspx";
	}
	else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}
}


/*
====================================================================================================
예매리아 클릭시 DB저장 호출
*/
function fnRiaOpen_Save(strValue) {

	var pageUrl = "/Reserve/riaOpenHistory.aspx?strPage=" + escape(location.href) + "&strString=" + escape(strValue);

	var xmlRequest = new ActiveXObject("Microsoft.XMLHTTP");
	xmlRequest.Open("GET", pageUrl, true);
	xmlRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	xmlRequest.onreadystatechange = function () { fnRiaOpen_CallBack(xmlRequest) };
	xmlRequest.Send(null);

	return xmlRequest;
}

function fnRiaOpen_CallBack(xmlRequest) {

	if (xmlRequest.readyState == 4) {

		if (xmlRequest.status == 200) {
			var strRtn = xmlRequest.responseBody;
		}

	}
}
/*
====================================================================================================
*/



// 티켓 교환권 출력
function FlashReserveTicket(reserve_id, reserve_no, pay_amt_type, movie_nm, theater_cd, theater_nm, screen_cd, seat_cd, play_ymd, start_hm, play_num, reserve_amt_tot, reserve_qty, member_nm, rating_cd, is_timo, prdt_nm) {
	var url = "/Reserve/print.aspx?"
				+ "reserve_Id=" + reserve_id			//예매ID
				+ "&reserve_no=" + reserve_no			//예매NO
				+ "&pay_amt_type=" + pay_amt_type			//결제유형
				+ "&movie_nm=" + movie_nm				//영화명
				+ "&theater_cd=" + theater_cd			//극장코드
				+ "&theater_nm=" + theater_nm			//극장명
				+ "&screen_cd=" + screen_cd				//상영관
				+ "&seat_cd=" + seat_cd				//좌석정보
				+ "&play_ymd=" + play_ymd				//상영일
				+ "&start_hm=" + start_hm				//상영시간
				+ "&play_num=" + play_num				//상영회차3
				+ "&reserve_amt_tot=" + reserve_amt_tot		//예매금액
				+ "&reserve_qty=" + reserve_qty			//예매수량
				+ "&member_nm=" + member_nm				//회원명
				+ "&rating_cd=" + rating_cd			    //영화등급
				+ "&is_timo=" + is_timo				//is timo
				+ "&prdt_nm=" + prdt_nm; 			//온라인매점

	TicketPrint = window.open(url, 'TicketPrint', 'width=657,height=600,scrollbars=yes');
}


// 초대장 보내기
function FlashReserveInvite(reserve_no, movie_cd, movie_nm, theater_cd, theater_nm, screen_cd, seat_cd, play_ymd, start_hm, play_num, reserve_qty, member_nm, email) {
	var url = "/Reserve/invite.aspx?"
				+ "reserve_no=" + reserve_no				//예매NO
				+ "&movie_cd=" + movie_cd				//영화코드
				+ "&movie_nm=" + movie_nm				//영화명
				+ "&theater_cd=" + theater_cd				//극장코드
				+ "&theater_nm=" + theater_nm				//극장명
				+ "&screen_cd=" + screen_cd				//상영관
				+ "&seat_cd=" + seat_cd					//좌석정보
				+ "&play_ymd=" + play_ymd				//상영일
				+ "&start_hm=" + start_hm				//시작시간
				+ "&play_num=" + play_num				//상영회차
				+ "&reserve_qty=" + reserve_qty				//예매수량			
				+ "&member_nm=" + member_nm				//회원명
				+ "&email=" + email; 				//이메일

	InvitationEMail = window.open(url, 'InvitationEMail', 'width=654,height=590,scrollbars=yes');
}

// 영수증 출력
function FlashReserveReceipt(hd_pg_ctrl_cd_p) { // 결재코드
	//영수증 출력
	var url = "http://newcgv.buymovie.co.kr/PgWeb/ui/receipt.aspx?controlNo=" + hd_pg_ctrl_cd_p;
	window.open(url, "receipt", 'toolbar=0,menubar=0,scrollbars=0,status=0,resizable=0,width=380,height=700');
}



// 인물정보 팝업에서 영화정보 링크
function movieDetail(movieIdx) {
	var url;
	url = "/movie/info/default.aspx?MovieIdx=" + movieIdx;
	if (opener != null) {
		if (opener.parent != null) {
			opener.parent.location.href = url;
		} else {
			opener.location.href = url;
		}
	} else {

		location.href = url;
	}
}




//예매완료후 리아에서 함수호출함
function callURL() {
	/*
	var url = "http://www.cgv.co.kr/event/developevent/091026_Event_MnetAward_PopUp..htm"
	window.open(url, "mama2009", 'toolbar=0,menubar=0,scrollbars=0,status=0,resizable=0,width=355,height=200');
	*/

	/*
	var url = "http://www.cgv.co.kr/popup/100129_pop_longView.html";
	window.open(url, "longview", 'toolbar=0,menubar=0,scrollbars=0,status=0,resizable=0,width=600,height=383');
	*/
	return;
}

// 상영시간표 관람등급 팝업창
function gradePopup() { uf_popOpen("/popup/p_theaterprice01.aspx"); }


function FlashReserveMain(args1, args2, args3, args4, args5, args6) {
	writeRiaObject(args1, args2);
}

// 간편예매
function writeSimple() {

writeRiaObject();
/*
	var riaobj;
	var moviePopObjFlash;

	riaobj = document.getElementById("ria_div");
	moviePopObjFlash = document.getElementById("movPlayerHtml");
	if (moviePopObjFlash) {
		document.getElementById("movPlayerHtml").style.display = "none";
		document.getElementById("movPlayerHtml").innerHTML = "";
	}

	if (riaobj) {
		riaobj.innerHTML = "";


		var fastTicket_HTML = "";
		fastTicket_HTML += '<object id="fscommand" data="data:application/x-silverlight-2," type="application/x-silverlight-2" width="260" height="320">';
		fastTicket_HTML += '<param name="source" value="http://newcgv.buymovie.co.kr/CGV2011Ria/ClientBin/CGVRiaSimple.xap"/>';
		fastTicket_HTML += '<param name="onError" value="onSilverlightError" />';
		fastTicket_HTML += '<param name="background" value="Transparent" />';
		fastTicket_HTML += '<param name="PluginBacground" value="Transparent" />';
		fastTicket_HTML += '<param name="Windowless" value="false" />';
		fastTicket_HTML += '<param name="minRuntimeVersion" value="4.0.50826.0" />';
		fastTicket_HTML += '<param name="enableHtmlAccess" value="true" />';
		fastTicket_HTML += '<param name="allowHtmlPopupWindow" value="true" />';
		fastTicket_HTML += '<param name="autoUpgrade" value="true" />';
		fastTicket_HTML += '<a href="http://go.microsoft.com/fwlink/?LinkID=149156&v=4.0.50826.0" style="text-decoration:none">';
		fastTicket_HTML += '<img src="http://go.microsoft.com/fwlink/?LinkId=161376" alt="Microsoft Silverlight 얻기" style="border-style:none"/></a>';
		fastTicket_HTML += '</object><iframe id="_sl_historyFrame" style="visibility:hidden;height:0px;width:0px;border:0px"></iframe>';


		riaobj.innerHTML = fastTicket_HTML;

		riaobj.style.display = "";

	} else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}

	document.documentElement.scrollTop = "0";
*/
}

var _S_TEXT01_ = "";
var _B_TEXT_ = "";



function isNaver(args1, args2, args3) {

writeRiaObject();
/*
	// 2011-11-11 Dbros Csk Attach
	// .ad_top_area 의 display 값이 block 일때 실행.
	if ($('.ad_top_area').css('display') == 'block') {
		// .ad_top_area 의 rel 값을 open으로 설정 한다
		$('.ad_top_area')
			.attr('rel', 'open')
			.slideUp('fast');
	}
	dimapp();

	var fastTicket_HTML = "";
	riaobj = document.getElementById("ria_div");
	moviePopObjFlash = document.getElementById("movPlayerHtml");
	if (moviePopObjFlash) {
		document.getElementById("movPlayerHtml").style.display = "none";
		document.getElementById("movPlayerHtml").innerHTML = "";
	}

	if (riaobj) {
		riaobj.innerHTML = "";


		if (args1 != null && args1 != "undefined") {
			try {
				CGVCode = args1.replace(/^\s-*-/, '').replace(/\s*$/, '');
				CGVCode = CGVCode.replace(' ', '');
				CGVCode = CGVCode.split("^");
				//RIAStr_Reserve = "&movie_cd1=" + CGVCode[0] + "&movie_cd2=" + CGVCode[1] + "&movie_cd3=" + CGVCode[2] + "&movie_cd4=" + CGVCode[3] + "&movie_cd5=" + CGVCode[4] + "&theaterCd=" + args2 + "&todayYMD=" + args3 + "&pay_code=11";
				//quickdata = _areacd + "|" + _theatercd + "|" + _movie_cd + "|" + _playymd + "|" + _screencd + "|" + _starttm + "|" + _a + "|" + _b;
				quickdata = "|" + args2 + "|" + CGVCode[0] + "|" + args3 + "||||";
			} catch (e) {
				//RIAStr_Reserve = "&movie_cd1=" + args1 + "&movie_cd2=&movie_cd3=&movie_cd4=&movie_cd5=&theaterCd=" + args2 + "&req_site=cgv&todayYMD=" + args3 + "&pay_code=11";
				quickdata = "|" + args2 + "|" + CGVCode[0] + "|" + args3 + "||||";
			}
		}
		else {
			RIAStr_Reserve = "";
		}


		fastTicket_HTML += '<object id="fscommand" data="data:application/x-silverlight-2," type="application/x-silverlight-2" width="1216" height="740">';
		fastTicket_HTML += '<param name="source" value="http://img.cgv.co.kr/CGV_RIA/2.7.3/RESERVATION_CLIENT.xap"/>';
		fastTicket_HTML += '<param name="onError" value="onSilverlightError" />';
		fastTicket_HTML += '<param name="background" value="Transparent" />';
		fastTicket_HTML += '<param name="PluginBacground" value="Transparent" />';
		fastTicket_HTML += '<param name="Windowless" value="false" />';
		fastTicket_HTML += '<param name="minRuntimeVersion" value="4.0.50826.0" />';
		fastTicket_HTML += '<param name="enableHtmlAccess" value="true" />';
		fastTicket_HTML += '<param name="allowHtmlPopupWindow" value="true" />';
		fastTicket_HTML += '<param name="autoUpgrade" value="true" />';
		fastTicket_HTML += '<param name="InitParams" value="_S_TEXT_=' + encodeURIComponent(_S_TEXT01_) + '' + ',_B_TEXT_=' + encodeURIComponent(_B_TEXT_) + '" /> ';
		fastTicket_HTML += '<a href="http://go.microsoft.com/fwlink/?LinkID=149156&v=4.0.50826.0" style="text-decoration:none">';
		fastTicket_HTML += '<img src="http://go.microsoft.com/fwlink/?LinkId=161376" alt="Microsoft Silverlight 얻기" style="border-style:none"/></a>';
		fastTicket_HTML += '</object><iframe id="_sl_historyFrame" style="visibility:hidden;height:0px;width:0px;border:0px"></iframe>';

		riaobj.innerHTML = fastTicket_HTML;
		riaobj.style.display = "";

	} else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}

	document.documentElement.scrollTop = "0";
*/
}


function isHana(args1, args2, args3) {

writeRiaObject();
/*
	var AreaCd;  // 지역코드
	var riaobj;
	var moviePopObjFlash;

	riaobj = document.getElementById("ria_div");
	moviePopObjFlash = document.getElementById("movPlayerHtml");
	if (moviePopObjFlash) {
		document.getElementById("movPlayerHtml").style.display = "none";
		document.getElementById("movPlayerHtml").innerHTML = "";
	}

	var ria = null;
	var fastTicket_HTML = "";

	var RIAStr;
	var RIAStr_Reserve;


	if (riaobj) {
		riaobj.innerHTML = "";

		if (args1 != null && args1 != "undefined") {
			try {
				CGVCode = args1.replace(/^\s*-/, '').replace(/\s*$/, '');
				CGVCode = CGVCode.replace(' ', '');
				CGVCode = CGVCode.split("^");
				RIAStr_Reserve = "&movie_cd1=" + CGVCode[0] + "&movie_cd2=" + CGVCode[1] + "&movie_cd3=" + CGVCode[2] + "&movie_cd4=" + CGVCode[3] + "&movie_cd5=" + CGVCode[4] + "&theaterCd=" + args2 + "&todayYMD=" + args3 + "&pay_code=11";
			} catch (e) {
				RIAStr_Reserve = "&movie_cd1=" + args1 + "&movie_cd2=&movie_cd3=&movie_cd4=&movie_cd5=&theaterCd=" + args2 + "&req_site=cgv&todayYMD=" + args3 + "&pay_code=11";
			}
		}
		else {
			RIAStr_Reserve = "";
		}


		if (document.cookie.length > 0) {
			RIAStr = "&isLogin1=True&isLogin=True&rsvCount=0&userName=" + getCookieRia2("UserName_RIA") + "&userId=" + getCookieRia2("UserId") + "&juminNum=" + getCookieRia2("Ssn_RIA") + "&email=" + getCookieRia2("Email_RIA") + "&runURL=http://www.cgv.co.kr&returnURL=" + location.href + "&phone=" + getCookieRia2("Phone_RIA") + "&phone_mobile=" + getCookieRia2("Mobile_RIA") + "&req_site=cgv&is_vip=" + getCookieRia2("IsVip") + "&is_cjvip=" + getCookieRia2("IsCJVip") + "&customer=" + getCookieRia2("FavoriteTheaters") + "&age=" + getCookieRia2("Age") + "&is_cgvemp=" + getCookieRia2("IsCgvEmployee") + "&Is_adult=" + getCookieRia2("IsAdult") + "&is_realssn=" + getCookieRia2("Ipin_realssn_YN");
		} else {
			RIAStr = "&isLogin1=&isLogin=out&rsvCount=&userName=&userId=&juminNum=&email=&runURL=http://www.cgv.co.kr&returnURL=" + location.href + "&phone=&phone_mobile=&req_site=cgv&is_vip=&is_cjvip=&customer=&age=&is_cgvemp=&Is_adult=&is_realssn=";
		}


		fastTicket_HTML += '<object id="fscommand" data="data:application/x-silverlight-2," type="application/x-silverlight-2" width="1216" height="740">';
		fastTicket_HTML += '<param name="source" value="http://img.cgv.co.kr/CGV_RIA/2.7.3/RESERVATION_CLIENT.xap"/>';
		fastTicket_HTML += '<param name="onError" value="onSilverlightError" />';
		fastTicket_HTML += '<param name="background" value="Transparent" />';
		fastTicket_HTML += '<param name="PluginBacground" value="Transparent" />';
		fastTicket_HTML += '<param name="Windowless" value="false" />';
		fastTicket_HTML += '<param name="minRuntimeVersion" value="4.0.50826.0" />';
		fastTicket_HTML += '<param name="enableHtmlAccess" value="true" />';
		fastTicket_HTML += '<param name="allowHtmlPopupWindow" value="true" />';
		fastTicket_HTML += '<param name="autoUpgrade" value="true" />';
		fastTicket_HTML += '<param name="InitParams" value="_S_TEXT_=' + encodeURIComponent(_S_TEXT01_) + '' + RIAStr + RIAStr_Reserve + ',_B_TEXT_=' + encodeURIComponent(_B_TEXT_) + '" /> ';
		fastTicket_HTML += '<a href="http://go.microsoft.com/fwlink/?LinkID=149156&v=4.0.50826.0" style="text-decoration:none">';
		fastTicket_HTML += '<img src="http://go.microsoft.com/fwlink/?LinkId=161376" alt="Microsoft Silverlight 얻기" style="border-style:none"/></a>';
		fastTicket_HTML += '</object><iframe id="_sl_historyFrame" style="visibility:hidden;height:0px;width:0px;border:0px"></iframe>';

		riaobj.innerHTML = fastTicket_HTML;
		riaobj.style.display = "";

		//Flash의 ExternalInterface가 Form Tag내에서 오류나는 버그를 해결하는 코드
		eval("window.fscommand = document.getElementById('fscommand');");


		// 리아히스토리
		fnRiaOpen_Save(RIAStr);

	} else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}

	document.documentElement.scrollTop = "0";
*/
}


function isSifff(args1, args2, args3) {

writeRiaObject();
/*
	var AreaCd;  // 지역코드
	var riaobj;
	var moviePopObjFlash;

	riaobj = document.getElementById("ria_div");
	moviePopObjFlash = document.getElementById("movPlayerHtml");
	if (moviePopObjFlash) {
		document.getElementById("movPlayerHtml").style.display = "none";
		document.getElementById("movPlayerHtml").innerHTML = "";
	}

	var ria = null;
	var fastTicket_HTML = "";

	var RIAStr;
	var RIAStr_Reserve;


	if (riaobj) {
		riaobj.innerHTML = "";

		if (args1 != null && args1 != "undefined") {
			try {
				CGVCode = args1.replace(/^\s*-/, '').replace(/\s*$/, '');
				CGVCode = CGVCode.replace(' ', '');
				CGVCode = CGVCode.split("^");
				RIAStr_Reserve = "&movie_cd1=" + CGVCode[0] + "&movie_cd2=" + CGVCode[1] + "&movie_cd3=" + CGVCode[2] + "&movie_cd4=" + CGVCode[3] + "&movie_cd5=" + CGVCode[4] + "&theaterCd=" + args2 + "&todayYMD=" + args3;
			} catch (e) {
				RIAStr_Reserve = "&movie_cd1=" + args1 + "&movie_cd2=&movie_cd3=&movie_cd4=&movie_cd5=&theaterCd=" + args2 + "&req_site=cgv&todayYMD=" + args3;
			}
		}
		else {
			RIAStr_Reserve = "";
		}


		if (document.cookie.length > 0) {
			RIAStr = "&isLogin1=True&isLogin=True&rsvCount=0&userName=" + getCookieRia("UserName_RIA") + "&userId=" + getCookieRia("UserId") + "&juminNum=" + getCookieRia("Ssn_RIA") + "&email=" + getCookieRia("Email_RIA") + "&runURL=http://www.cgv.co.kr&returnURL=" + location.href + "&phone=" + getCookieRia("Phone_RIA") + "&phone_mobile=" + getCookieRia("Mobile_RIA") + "&req_site=cgv&is_vip=" + getCookieRia("IsVip") + "&is_cjvip=" + getCookieRia("IsCJVip") + "&customer=" + getCookieRia("FavoriteTheaters") + "&age=" + getCookieRia("Age") + "&is_cgvemp=" + getCookieRia("IsCgvEmployee") + "&Is_adult=" + getCookieRia("IsAdult") + "&is_realssn=" + getCookieRia("Ipin_realssn_YN");
		} else {
			RIAStr = "&isLogin1=&isLogin=out&rsvCount=&userName=&userId=&juminNum=&email=&runURL=http://www.cgv.co.kr&returnURL=" + location.href + "&phone=&phone_mobile=&req_site=cgv&is_vip=&is_cjvip=&customer=&age=&is_cgvemp=&Is_adult=&is_realssn=";
		}


		fastTicket_HTML += '<object id="fscommand" data="data:application/x-silverlight-2," type="application/x-silverlight-2" width="1216" height="740">';
		fastTicket_HTML += '<param name="source" value="http://img.cgv.co.kr/CGV_RIA/2.7.3/RESERVATION_CLIENT.xap"/>';
		fastTicket_HTML += '<param name="onError" value="onSilverlightError" />';
		fastTicket_HTML += '<param name="background" value="Transparent" />';
		fastTicket_HTML += '<param name="PluginBacground" value="Transparent" />';
		fastTicket_HTML += '<param name="Windowless" value="false" />';
		fastTicket_HTML += '<param name="minRuntimeVersion" value="4.0.50826.0" />';
		fastTicket_HTML += '<param name="enableHtmlAccess" value="true" />';
		fastTicket_HTML += '<param name="allowHtmlPopupWindow" value="true" />';
		fastTicket_HTML += '<param name="autoUpgrade" value="true" />';
		fastTicket_HTML += '<param name="InitParams" value="_S_TEXT_=' + encodeURIComponent(_S_TEXT01_) + '' + RIAStr + RIAStr_Reserve + ',_B_TEXT_=' + encodeURIComponent(_B_TEXT_) + '" /> ';
		fastTicket_HTML += '<a href="http://go.microsoft.com/fwlink/?LinkID=149156&v=4.0.50826.0" style="text-decoration:none">';
		fastTicket_HTML += '<img src="http://go.microsoft.com/fwlink/?LinkId=161376" alt="Microsoft Silverlight 얻기" style="border-style:none"/></a>';
		fastTicket_HTML += '</object><iframe id="_sl_historyFrame" style="visibility:hidden;height:0px;width:0px;border:0px"></iframe>';

		riaobj.innerHTML = fastTicket_HTML;
		riaobj.style.display = "";

		//Flash의 ExternalInterface가 Form Tag내에서 오류나는 버그를 해결하는 코드
		eval("window.fscommand = document.getElementById('fscommand');");


		// 리아히스토리
		fnRiaOpen_Save(RIAStr);

	} else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}

	document.documentElement.scrollTop = "0";
*/
}

function changeLayerSize(id, tw, th) {

	var obj = document.getElementById(id);
	if (obj) {
		obj.style.width = tw + "px";
		obj.style.height = th + "px";
	}
}

function thisMovie(movieName) {
	if (navigator.appName.indexOf("Microsoft") != -1) {
		return window[movieName];
	} else {
		return document[movieName];
	}
}

// 리아에서 선호극장 팝업
function openTheaterRIA() {
	var url;
	url = "/Reserve/favoriteTheater.aspx?from=flash";
	window.open(url, 'openFavoriteTheater', 'toolbar=0,menubar=0,scrollbars=no,resizable=no,width=265,height=405;')
}


//영화상세플래시팝업
function mainMoviePopup(movieidx) {
	var movieObj = document.getElementById("movie_div");

	var so = new SWFObject("/common/flash/main/detailPopup.swf", "mainMovepop", "710", "420", "", "#ffffff");
	so.addParam("wmode", "transparent");
	so.addVariable("wsURL", "http://service.cgv.co.kr/movie/movie2.asmx");
	so.addVariable("movieIndex", movieidx);
	so.write("movie_div");

	movieObj.style.display = "";
}

//영화상세플래시팝업 닫기
function closeMoviePopup() {
	document.getElementById("movPlayerHtml").style.display = "none";
	document.getElementById("movPlayerHtml").innerHTML = "";
}

//영화상세 무비클립, 스틸컷 링크
function setMovieClip(movieIdx, clipIdx, curList) {
	var url = "/movie/info/default.aspx?tabIdx=3";
	if (clipIdx == "") {
		url += "&MovieIdx=" + movieIdx + "&curList=" + curList;
	} else {
		url += "&MovieIdx=" + movieIdx + "&curList=" + curList + "&ClipIdx=" + clipIdx;
	}
	var fname = frameElement.name;

	if (fname != "f_mov") {
		location.href = url;
	} else {
		parent.location.href = url;
	}
}

//퍼가기 :
function getCopy(movieIdx) {
	popfix("/movie/info/scrap.aspx?MovieIdx=" + movieIdx, 'scrap', 660, 670, 1);
	//	uf_popOpen("/movie/info/scrap.aspx?MovieIdx=" + movieIdx, "scrap");
}

//찜하기 :
function getZzim(movieIdx) {
	/*
	var fname = frameElement.name;
	if (fname == "f_mov") {     
	parent.location.href = parent.$n("loginCheckLink").href;
	}
	else {
	location.href = $n("loginCheckLink").href;
	}
	*/
	if (frameElement != null && frameElement.name == "f_mov") {
		parent.location.href = parent.$n("loginCheckLink").href;
	}
	else {
		location.href = $n("loginCheckLink").href;
	}
}

//CGVian 리뷰쓰기 :
function setReview(movieIdx) {
	var fname = frameElement.name;
	if (fname != "f_mov")
		location.href = "/openreview/cgvian/cgvian_write.aspx?MovieIdx=" + movieIdx;
	else
		parent.location.href = "/openreview/cgvian/cgvian_write.aspx?MovieIdx=" + movieIdx;
}
//평점쓰기 :
function setRating(movieIdx) {
	var fname = frameElement.name;
	if (fname != "f_mov")
		location.href = "/openreview/rating/rating_detail.aspx?MovieIdx=" + movieIdx;
	else
		parent.location.href = "/openreview/rating/rating_detail.aspx?MovieIdx=" + movieIdx;
}

//명대사쓰기 :
function setScript(movieIdx) {
	var fname = frameElement.name;
	if (fname != "f_mov")
		location.href = "/movie/info/default.aspx?MovieIdx=#{movieIdx}&tabIdx=4&reviewIdx=best".interpolate({ movieIdx: movieIdx });
	else
		parent.location.href = "/movie/info/default.aspx?MovieIdx=#{movieIdx}&tabIdx=4&reviewIdx=best".interpolate({ movieIdx: movieIdx });
}

//인물정보 팝업
function popPeople(peopleIdx) {
	uf_popOpen("/movie/info/people.aspx?peopleIdx=" + peopleIdx, "people");
	//	popfix("/movie/info/people.aspx?peopleIdx=" + peopleIdx, "people", 460, 356, 0);
}


function awardInfo() {
	alert("당첨자 안내");
}

function awardVote(type) {
	switch (type) {
		case 0:
			alert("이달의 영화인 투표");
			break;
		case 1:
			alert("이달의 영화인 투표");
			break;
		default:
			alert("알수 없음");
			break;
	}
}

function moreHonor() {
	alert("명예의 전당 more");
}

// 마이시지브 배너 링크
function watchMovie(args) {
	switch (args) {
		case "0":
			//location.href = "/mycgv/point/default.aspx";
			location.href = "/user/membership/default.aspx?tabindex=4";
			break;
		case "1":
			//location.href = "/mycgv/diary/coupon/movie/list.aspx";
			location.href = "/gift/ticket/buy.aspx";
			break;
		case "2":
			//location.hef = "/mycgv/gift/gift01.aspx";
			location.href = "/reservation/ticket/ticket.aspx";
			break;
		case "3":
			location.href = "/reservation/card/ACard.aspx";
			break;
		case "4":
			location.href = "/mycgv/diary/coupon/reserve/list.aspx";
			break;
		default:
			location.href = "/mycgv/point/default.aspx";
			break;
	}

}


//당첨자 안내 		
function awardInfo() {
	location.href = "/event/winner/list.aspx";
}

//	이달의 영화투표0- 영화, 1- 영화인
function awardVote(args) {

	switch (args) {
		case 0:
			location.href = "/openreview/cgvaward/cgvaward1.aspx";
			break;
		case 1:
			location.href = "/openreview/cgvaward/cgvaward2.aspx";
			break;
		default:
			location.href = "/openreview/cgvaward/cgvaward1.aspx";
			break;
	}
}

//	명예의전당more 		
function moreHonor() {
	location.href = "/openreview/cgvaward/cgvaward3.aspx";
}


function magazineTab(args) {
	switch (args) {
		case 0:
			location.href = "/magazine/magazine/default.aspx?MovieNCode=1301";
			break;
		case 1:
			location.href = "/magazine/magazine/default.aspx?MovieNCode=1302";
			break;
		case 2:
			location.href = "/magazine/magazine/default.aspx?MovieNCode=1303";
			break;
		case 3:
			location.href = "/magazine/magazine/default.aspx?MovieNCode=1304";
			break;
		case 4:
			location.href = "/magazine/magazine/default.aspx?MovieNCode=1315";
			break;
		case 5:
			location.href = "/magazine/news/default.aspx";
			break;
		case 6:
			location.href = "/magazine/media/default.aspx";
			break;
		case 7:
			location.href = "/magazine/weekend/default.aspx";
			break;
		default:
			location.href = "/magazine/default.aspx";
			break;
	}

}

//*********************************** 실버라이트 영역
// 실버라이트빠른예매 writeRiaObject 실버라이트 가능하도록 변경
function writeRiaObject(args1, args2) {

	var MOVIE_CD = "";

	if (args1 != null && args1 != "undefined") {


		try {
			CGVCode = args1.replace(/^\s*/, '').replace(/\s*$/, '');
			CGVCode = CGVCode.replace(' ', '');
			CGVCode = CGVCode.split("^");

			MOVIE_CD = CGVCode[0];

		} catch (e) {
			MOVIE_CD = args1;
		}
	}

	if (IsMobile())
	{
		top.location.href = "http://m.cgv.co.kr/QuickReservation/";
	}
	else
	{
		location.href = "http://www.cgv.co.kr/ticket/?MOVIE_CD=" + MOVIE_CD + "&MOVIE_CD_GROUP=" + MOVIE_CD + "&PLAY_YMD=&THEATER_CD=&PLAY_NUM=&PLAY_START_TM=&AREA_CD=&SCREEN_CD=";
	}
}


// 리아 비회원
function GuestLogin() {
	location.href = "/user/guest/login_guest.aspx";
}

// 예매 확인 비회원
function GuestReserveConfirm(name, ssn) {

	var keyObject = document.getElementById("loginform");

	if (keyObject) {
		document.loginform.method = "post";
		document.loginform.id.value = name;
		document.loginform.password.value = ssn;
		document.loginform.returnURL.value = "AA";
		document.loginform.action = "/user/guest/GuestMember.aspx";
		document.loginform.submit();
	}
	else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}
}

function GuestTicketing() {
	if (getCookieGuest("gSSN").length > 0) {
		GuestRiaObject(getCookieGuest("gUserName")
			, getCookieGuest("gUserID")
			, getCookieGuest("gSSN")
			, getCookieGuest("gAge")
			, getCookieGuest("gIsAdult")
			, getCookieGuest("Phone_RIA")
			, getCookieGuest("Mobile_RIA")
		);
	}
	else {
		GuestLogin();
	}

}

function GuestReserve() {
	var keyObject = document.getElementById("loginform");

	if (keyObject) {
		document.loginform.method = "post";
		document.loginform.id.value = getCookieGuest("gUserName");
		document.loginform.password.value = getCookieGuest("gSSN");
		document.loginform.returnURL.value = "AA";
		document.loginform.action = "/user/guest/GuestMember.aspx";
		document.loginform.submit();
	}
	else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}
}


function getCookieGuest(_cookieName) {
	var currcookie = setCookieNodecode("cgv.cookie.Guest");

	var cookieList = currcookie.split("&");
	var cookieValue = "";
	for (i = 0; i < cookieList.length; i++) {
		if (cookieList[i].indexOf(_cookieName + "=") > -1) {
			if (cookieList[i].split("=")[0].replace(/\s/g, "") == _cookieName) {
				cookieValue = cookieList[i].split("=")[1];
				break;
			}
		}
	}

	return cookieValue;
}



// 비회원 예매가 가능하도록 실버라이트 수정
function GuestRiaObject(sUserName_Ria, sUserID, sSSN_Ria, sAge, sIsAdult, sPhone, sMobile) {

writeRiaObject();

/*
	//var height=1905;
	dimapp();

	//=========================================================================
	//실버라이트확인을 위한 개발작업 S
	//=========================================================================
	try {
	    if (SilverLightBrowserVersion() == true) {
	        return;
	    }
	}
	catch (ex) { }
	//=========================================================================
	//실버라이트확인을 위한 개발작업 E
	//=========================================================================

	//wrapMask();
	// 111004 attach CSK RIA닫을때 아래 레이어 hidden
	// visible 소스는 jq.default.js 1073행
	if ($('.top_player').length > 0) { $('.top_player').css({ "visibility": 'hidden' }) }
	$('#TopBanner').css({ "visibility": 'hidden' });
	$('#ADSmallWrapper').css({ "visibility": 'hidden' });
	$('#ADSmallWrapper2').css({ "visibility": 'hidden' });
	$('#ADShowRWrapper').css({ "visibility": 'hidden' });
	var strPartner = "cgv";
	try {
		if (getCookieCommon("cgv.cookie.Reserve").indexOf("partner=benepia") != -1) {
			strPartner = "benepia";
		}
	}
	catch (ex) {
		strPartner = "cgv"
	}

	var riaobj;
	var moviePopObjFlash;

	riaobj = document.getElementById("ria_div");
	moviePopObjFlash = document.getElementById("movPlayerHtml");
	if (moviePopObjFlash) {
		document.getElementById("movPlayerHtml").style.display = "none";
		document.getElementById("movPlayerHtml").innerHTML = "";
	}

	var ria = null;
	var fastTicket_HTML = "";
	var dtNow = new Date();
	var todayYMD = dtNow.getFullYear() + "" + dtNow.getMonth() + "" + dtNow.getDay();

	var gRIAStr;
	var gRIAStr_Reserve;
	var AreaCD, TheaterCD = "";

	try {
		RegionArea = getRegionArea();
		AreaCD = RegionArea.split("|")[0];
		TheaterCD = RegionArea.split("|")[1];
	}
	catch (ex) {
		AreaCD = "13";
		TheaterCD = "0056";
	}

	if (riaobj) {
		riaobj.innerHTML = "";

		if (sUserName_Ria == "") sUserName_Ria = getCookieGuest("gUserName");
		if (sUserID == "") sUserID = getCookieGuest("gUserID");
		if (sSSN_Ria == "") sSSN_Ria = getCookieGuest("gSSN");
		if (sAge == "") sAge = getCookieGuest("gAge");
		if (sIsAdult == "") sIsAdult = getCookieGuest("gIsAdult");
		if (sPhone == "") sPhone = getCookieGuest("Phone_RIA");
		if (sMobile == "") sMobile = getCookieGuest("Mobile_RIA");


		gRIAStr = "isGuest=True,isLogin1=True,isLogin=True,rsvCount=0,userName=" + sUserName_Ria 
			+ ",userId=" + sUserID + ",juminNum=" + sSSN_Ria + ",email=,runURL=http://www.cgv.co.kr,returnURL=" + location.href 
			+ ",phone=" + sPhone 
			+ ",phone_mobile=" + sMobile
			+ ",req_site=cgv,is_vip=N,is_cjvip=N,is_cjent=N,customer=,age=" + sAge + ",is_cgvemp=N,Is_adult=" + sIsAdult + ",is_realssn=Y,is_cjms=1,Area=" + AreaCD + ",Theater=" + TheaterCD;
		gRIAStr_Reserve = "";


		fastTicket_HTML += '<object id="fscommand" data="data:application/x-silverlight-2," type="application/x-silverlight-2" width="1216" height="740">';
		fastTicket_HTML += '<param name="source" value="http://img.cgv.co.kr/CGV_RIA/2.7.3/RESERVATION_CLIENT.xap"/>';
		fastTicket_HTML += '<param name="onError" value="onSilverlightError" />';
		fastTicket_HTML += '<param name="background" value="Transparent" />';
		fastTicket_HTML += '<param name="PluginBacground" value="Transparent" />';
		fastTicket_HTML += '<param name="Windowless" value="false" />';
		fastTicket_HTML += '<param name="minRuntimeVersion" value="4.0.50826.0" />';
		fastTicket_HTML += '<param name="enableHtmlAccess" value="true" />';
		fastTicket_HTML += '<param name="allowHtmlPopupWindow" value="true" />';
		fastTicket_HTML += '<param name="autoUpgrade" value="true" />';
		fastTicket_HTML += '<param name="InitParams" value="' + gRIAStr + gRIAStr_Reserve + '" /> ';
		fastTicket_HTML += '<a href="http://go.microsoft.com/fwlink/?LinkID=149156&v=4.0.50826.0" style="text-decoration:none">';
		fastTicket_HTML += '<img src="http://go.microsoft.com/fwlink/?LinkId=161376" alt="Microsoft Silverlight 얻기" style="border-style:none"/></a>';
		fastTicket_HTML += '</object><iframe id="_sl_historyFrame" style="visibility:hidden;height:0px;width:0px;border:0px"></iframe>';


		riaobj.innerHTML = fastTicket_HTML;
		riaobj.style.display = "";

		eval("window.fscommand = document.getElementById('fscommand');");

		//=========================================================================
		//마이너체인지 팝업 2011.12.26
		//=========================================================================
		try {
			if (getCookieMinor("MinorChangePopupCheck") != "1")
				minorChangePopup();
		}
		catch (ex) { }
		//=========================================================================
		//마이너체인지 팝업 2011.12.26
		//=========================================================================


		// 리아히스토리
		fnRiaOpen_Save(gRIAStr);

	} else {
		alert("진행중입니다. 화면이 완료된 후에 클릭해주세요.");
		document.location.reload();
	}

	document.documentElement.scrollTop = "0";
*/
}


var msxmlNames = new Array("MSXML2.XMLHTTP.4.0", "MSXML2.XMLHTTP.3.0", "MSXML2.XMLHTTP", "Microsoft.XMLHTTP");
function getXMLHTTPRequestRia() {
	if (window.ActiveXObject) {
		for (var i = 0; i < this.msxmlNames.length; i++) {
			try {
				return new ActiveXObject(this.msxmlNames[i]);
			} catch (e) { }
		}
	} else if (window.XMLHttpRequest) {
		/* Mozilla XMLHttpRequest */
		return new XMLHttpRequest();
	} else {
		/* None found */
		return null;
	}
}


function getRegionArea() {
	var Url = "/Reserve/RegionIP.aspx";
	var xmlRequest = getXMLHTTPRequestRia();
	xmlRequest.open("GET", Url, false);
	xmlRequest.send(null);

	if (xmlRequest.readyState == 4) {
		if (xmlRequest.status == 200) {
			//요청한값 확인하기
			var rst = xmlRequest.responseText;
		}
		else {
			//alert("Error while retrieving data!");
			return "13";
		}
	}

	return rst
}

function getRegionCode(type) {
	var Url = "/Reserve/RegionCode.aspx?tcode=" + type;
	return getXmlReqData(Url)
}

function getXmlReqData(Url) {
	var xmlRequest = getXMLHTTPRequestRia();
	xmlRequest.open("GET", Url, false);
	xmlRequest.send(null);

	if (xmlRequest.readyState == 4) {
		if (xmlRequest.status == 200) {
			var rst = xmlRequest.responseText;
		}
		else {
			//alert("Error while retrieving data!");
			return "";
		}
	}

	return rst
}

function getXmlRiaMovieInfo(mcd) {
	var Url = "/Reserve/RiaMovieInfo.aspx?mcd=" + mcd;
	return getXmlReqData(Url)
}


function getRiaAdUrl(type) {
	var Url = "/Reserve/GetRiaADUrl.aspx?AdType=" + type;
	return getXmlReqData(Url)
}


function setADRia(AdType) {

	var AdWidth = "";
	var AdHeight = "";
	var ImgUrl = "";
	var LinkUrl = "";
	var AdUrl = getRiaAdUrl(AdType);

	if (AdUrl != "") {
		var arrAdUrl = AdUrl.split("|")

		AdWidth = arrAdUrl[0].split("=")[1];
		AdHeight = arrAdUrl[1];
		ImgUrl = arrAdUrl[3];
		LinkUrl = arrAdUrl[4];

		document.getElementById('ria_div_ad').style.width = "1216px";
		document.getElementById('ria_div_ad').style.height = "740px";
		document.getElementById('ria_div_ad').style.background = " url(" + ImgUrl + ") bottom right no-repeat";
		document.getElementById("ria_div_ad").onclick = function () { window.open(LinkUrl); }
		document.getElementById("ria_div_ad").style.cursor = "hand";

	}
}



function GetRiaMovieInfo(CgvCD) {
	var midx = getXmlRiaMovieInfo(CgvCD);
	var LinkUrl = "";
	var myWin;

	try {
		trk_flashEnvView('_TRK_PI=TTI', '_TRK_CP=/예매 메인/STEP1-영화정보', '_TRK_DU=/movie/popup/ria_MovieInfo.aspx');
	}
	catch (ex) { }

	if (midx == "") {
		LinkUrl = "/movie/popup/ria_MovieInfo_Notfound.html";
		myWin = window.showModalDialog(LinkUrl, "winName", "dialogWidth:630px;dialogHeight:325px; center:yes; help:no; status:no; scroll:no; resizable:no");
	}
	else {
		LinkUrl = "/movie/popup/ria_MovieInfo.aspx?CGVCode=" + CgvCD;
		myWin = window.showModalDialog(LinkUrl, "winName", "dialogWidth:630px;dialogHeight:325px; center:yes; help:no; status:no; scroll:no; resizable:no");
	}
}

function GetRiaTheaterInfo(TheaterCode, OnlyOneCode) {
	if (OnlyOneCode == undefined) {
		OnlyOneCode = "";
	}
	else {
		OnlyOneCode = "&ScreenCode=" + OnlyOneCode;
	}

	try {
		trk_flashEnvView('_TRK_PI=TMI', '_TRK_CP=/예매 메인/STEP1-극장정보', '_TRK_DU=/movie/popup/ria_TheaterInfo.aspx');
	}
	catch (ex) { }


	var LinkUrl = "/movie/popup/ria_TheaterInfo.aspx?TheaterCode=" + TheaterCode + OnlyOneCode;
	var myWin = window.showModalDialog(LinkUrl, "winName", "dialogWidth:807px;dialogHeight:500px; center:yes; help:no; status:no; scroll:yes; resizable:no");
}


//=========================================================================
//실버라이트확인을 위한 개발작업
//=========================================================================
function popupQuickMini() {
	var w = 440;
	var h = 740;
	var l = (screen.width - w) / 2;
	var t = 20;
	var qmini = window.open('/mini/User/Login.aspx', 'qmini', 'left=' + l + ',top=' + t + ',menubar=1,resizable=1,width=' + w + ',height=' + h + ',scrollbars=1');
	//        qmini.moveTo(350, 10);
}
function popupQuickMiniForce() {
    var w = 440;
    var h = 740;
    var l = (screen.width - w) / 2;
    var t = 20;
    var qmini = window.open('/mini/User/Notice.aspx', 'qmini', 'left=' + l + ',top=' + t + ',menubar=1,resizable=1,width=' + w + ',height=' + h + ',scrollbars=1');
    closeSilverLightPopup();
    return true;
}
function checkSilverLight(obj) {
	try {
		var riaImg1 = '<div class="wrapper" style="position:relative; width:960px; margin:0 auto;">';
		riaImg1 += '	<img src="http://img.cgv.co.kr/Event/ImagesEvent/1201/120104_siverlight_event1.jpg" alt="" border="0" usemap="#Map" style="vertical-align:top;"/>';
		riaImg1 += '	<map name="Map" id="Map">';
		riaImg1 += '		<area shape="rect" coords="908,7,955,48" href="javascript:closeSilverLightPopup();" alt="닫기" />';
		riaImg1 += '		<area shape="rect" coords="787,245,825,271" href="javascript:popupQuickMini();" alt="빠른예매 미니" />';
		riaImg1 += '		<area shape="rect" coords="340,675,622,741" href="http://www.microsoft.com/downloads/ko-kr/details.aspx?displaylang=ko&FamilyID=049C9DBE-3B8E-4F30-8245-9E368D3CDB5A" alt="서비스팩2 다운받기" target="_blank" />';
		riaImg1 += '	</map>';
		riaImg1 += '</div>';

		var riaImg2 = '<div class="wrapper" style="position:relative; width:960px; margin:0 auto;"><img src="http://img.cgv.co.kr/event/ImagesEvent/120409/120409_siverlight_event.jpg" alt="" border="0" usemap="#Map" style="vertical-align:top;"/>';
		riaImg2 += '	<map name="Map" id="Map">';
		riaImg2 += '		<area shape="rect" coords="540,260,571,277" href="javascript:popupQuickMini();" alt="빠른예매 미니" />';
		riaImg2 += '		<area shape="rect" coords="378,366,641,419" href="http://www.microsoft.com/getsilverlight/handlers/getsilverlight.ashx" alt="실버라이트 다운받기" target="_blank" />';
		riaImg2 += '		<area shape="rect" coords="536,596,669,613" href="javascript:popupQuickMini();" alt="빠른예매 미니" />';
		riaImg2 += '		<area shape="rect" coords="208,736,242,754" href="/support/faq/Default.aspx" target="_blank" alt="FAQ" />';
		riaImg2 += '		<area shape="rect" coords="325,784,355,802" href="javascript:popupQuickMini();" alt="빠른예매 미니" />';
		riaImg2 += '		<area shape="rect" coords="296,974,327,993" href="javascript:popupQuickMini();" alt="빠른예매 미니" />';
		riaImg2 += '	</map>';
		riaImg2 += '</div>';

		var _bool = Silverlight.isInstalled(null);
		var riaobj = document.getElementById("ria_div");
		if (_bool == false) {
			riaobj.innerHTML = eval(obj);
			riaobj.style.display = "";
			return true;
		}

	}
	catch (ex) {
	}
}
//2013.05.07
function callChrome(){
		/*
		$(".close_ria2").click(function () {
			if($('#cbSilverChrome').is(':checked')){
				setCookie('SilverChrome', 'done', 30);
			}
            closeSilverLightPopup();
            return false;
        });
		*/
        $(".view_system").click(function () {
            $(".pop_view_system1").fadeIn()
            return false;
        });
        $(".pop_view_system1").hide();
        $(".close_pop_vs").click(function () {
            $(this).parents(".pop_view_system1").fadeOut(200)
            return false;
        });
	}

function closeSilverLightPopup() {
	var riaobj = document.getElementById("ria_div");
	riaobj.innerHTML = '';
	$('.mini').hide();
	$('.pop_view_system1').hide();
	$('.lyRiaWrap').find('.mask').fadeOut('fast');
}

//=========================================================================
//마이너체인지 팝업 2011.12.26 S
//=========================================================================
function minorChangePopup(){
	var userAgent = window.navigator.userAgent;
	var minorPopHtml = '<div id="minorChangePopup" style="width:981px; height:30px; padding-top:495px;">'
									+ '	<p><img src="http://img.cgv.co.kr/images/popup/120220_ria_layer.png" alt="" style="font-size:0; line-height:0; position:absolute; left:-27px; top:0;" /><a id="popRiaPopOpen" style="position:absolute; bottom:90px; right:108px; z-index:99;" href="#"><img src="http://img.cgv.co.kr/images/popup/btn_ria_layer2.gif" alt=""/></a></p>'
									+ '	<div class="popupInpop" style="display:none;position:absolute;top:30px;left:95px;z-index:500;"><img src="http://img.cgv.co.kr/images/popup/popupInpop.gif" alt=""/><a id="popRiaPopClose" style="position:absolute; top:15px; right:16px; z-index:99;" href="#"><img src="http://img.cgv.co.kr/images/popup/btn_popupInpop_close.gif" alt=""/></a></div>'
									+ '	<div style="clear:both; width:100%; text-align:center; height:73px; color:#E0DED9; background:#1c1c1c; border-bottom:3px solid #e22213;">'
									+ '		<div style="width:300px; margin:0 auto; padding:10px 0 0 0;  text-align:center;"><input type="checkbox" id="cbMinorChangePop" name="chkbox" style="width:13px;height:13px;margin:8px 0 2px 0;padding:0;vertical-align:top;"> '
									+ '			<img src="http://img.cgv.co.kr/images/popup/111222_ria_layer_img1.png" alt="" />'
									+ '			<a href="javascript:closeMinorChangePopup();"><img src="http://img.cgv.co.kr/images/popup/111222_ria_layer_img2.png" alt="" style="vertical-align:top" />'
									+ '		</div>'
									+ '	</div>'
									+ '</div>';

	var minorPopHtml2 = '<div id="minorChangePopup" style="width:981px; height:30px; padding-top:495px;">'
									+ '	<img src="http://img.cgv.co.kr/common/silverlight/system_chk/bg_system.png" usemap="#Map1" alt="" style="font-size:0; line-height:0; position:absolute; left:-27px; top:0;" />'
									+ '		<map name="Map1">'
									+ '			<area shape="rect" coords="594,229,760,265" href="#" class="view_system"/>'
									+ '			<area shape="rect" coords="486,305,626,330" href="javascript:openMiniRia(); " target="_blank" alt="Mini 예매 바로가기"/>'
									+ '			<area shape="rect" coords="485,357,626,383" href="http://nstore.naver.com/search/search.nhn?t=apps&fs=default&q=CGV+%EC%98%81%ED%99%94%EC%98%88%EB%A7%A4" target="_blank" alt="APP 다운 받으러 가기"/>'
									+ '		</map>'
									+ '	<div class="popupInpop" style="display:none;position:absolute;top:30px;left:95px;z-index:500;"><img src="http://img.cgv.co.kr/images/popup/popupInpop.gif" alt=""/><a id="popRiaPopClose" style="position:absolute; top:15px; right:16px; z-index:99;" href="#"><img src="http://img.cgv.co.kr/images/popup/btn_popupInpop_close.gif" alt=""/></a></div>'
									+ '	<div style="clear:both; width:100%; text-align:center; height:73px; color:#E0DED9; background:#1c1c1c; border-bottom:3px solid #e22213;">'
									+ '		<div style="width:300px; margin:0 auto; padding:10px 0 0 0;  text-align:center;"><input type="checkbox" id="cbMinorChangePop" name="chkbox" style="width:13px;height:13px;margin:8px 0 2px 0;padding:0;vertical-align:top;"> '
									+ '			<img src="http://img.cgv.co.kr/images/popup/111222_ria_layer_img1.png" alt="" />'
									+ '			<a href="javascript:closeMinorChangePopup();"><img src="http://img.cgv.co.kr/images/popup/111222_ria_layer_img2.png" alt="" style="vertical-align:top" />'
									+ '		</div>'
									+ '	</div>'
									+ '</div>'
									+ '<div class="pop_view_system1">'
									+ '	<img src="http://img.cgv.co.kr/common/silverlight/system_chk/pop_view_system.jpg" border="0" usemap="#Map2" />'
									+ '	<map name="Map2">'
									+ '		<area shape="rect" coords="539,6,565,28" href="#" class="close_pop_vs">'
									+ '	</map>'
									+ '</div>';
	
	$("#ria_div").hide();
	$("#silver").hide();
	document.getElementById("minorPopup").innerHTML = userAgent.indexOf("Chrome") == -1 ? minorPopHtml : minorPopHtml2;
	//document.getElementById("minorPopup").innerHTML = minorPopHtml;

	if(userAgent.indexOf("Chrome") != -1)
		callChrome();

	$('#popRiaPopOpen').click(function(){
		$('.popupInpop').fadeIn();
	})
	$('#popRiaPopClose').click(function(){
		$('.popupInpop').fadeOut();
	})

}

function getCookieMinor(name) {
	var nameOfCookie = name + "=";
	var x = 0;
	while (x <= document.cookie.length) {
		var y = (x + nameOfCookie.length);
		if (document.cookie.substring(x, y) == nameOfCookie) {
			if ((endOfCookie = document.cookie.indexOf(";", y)) == -1)
				endOfCookie = document.cookie.length;
			return unescape(document.cookie.substring(y, endOfCookie));
		}
		x = document.cookie.indexOf(" ", x) + 1;
		if (x == 0)
			break;
	}
	return "";
}

function setCookieMinor(name, value, expiredays) {
	var todayDate = new Date();
	todayDate.setDate(todayDate.getDate() + expiredays);
	document.cookie = name + "=" + escape(value) + "; path=/; expires=" + todayDate.toGMTString() + ";"
}

function MinorChangePopupCheck() {
	if ($("#cbMinorChangePop").is(":checked")) {
		setCookieMinor("MinorChangePopupCheck", "1", 100);
		closeMinorChangePopup();
	}
	$('.pop_view_system1').hide();
}

function closeMinorChangePopup() {
	if ($("#cbMinorChangePop").is(":checked")) {
		setCookieMinor("MinorChangePopupCheck", "1", 100);
	}
	$("#minorChangePopup").remove();
	$("#ria_div").show();
	$('.pop_view_system1').hide();
}


//=========================================================================
//마이너체인지 팝업 2011.12.26 E
//=========================================================================

//
//USER AGENT 체크 실버라이트 미설치, 서비스팩2
//
function SilverLightBrowserVersion() {
	//윈도우 2000 : MSIE 5.5;Windows NT 5.0, 윈도우ME : MSIE 5.5;Windows 98
	var userAgent = window.navigator.userAgent;

	//윈도우OS
	if (userAgent.indexOf("Windows") != -1) {
		//2000, 윈도우98, ME
		if (userAgent.indexOf("MSIE 5.5") != -1) {
			//윈도우2000은 서비스팩4부터 실버라이트 지원
			if (userAgent.indexOf("Windows NT 5.0") != -1) {
			    return popupQuickMiniForce();
			}
			//윈98, 윈 ME 체크 Win 9x 
			else if (userAgent.indexOf("Windows 98") != -1 || userAgent.indexOf("Win 9") != -1) {
			    return popupQuickMiniForce();
			}
            else
                return popupQuickMiniForce();
		}
		//윈도우 XP 익스 6
		else if (userAgent.indexOf("Windows NT 5.1") != -1 && userAgent.indexOf("MSIE 6.0") != -1) {
			if (userAgent.indexOf("SV1") != -1) {
				return checkSilverLight('riaImg2');
			}
			else {
				return checkSilverLight('riaImg1');
			}
		}
		//익스 7이상
		else if (userAgent.indexOf("MSIE 7") != -1 || userAgent.indexOf("MSIE 8") != -1 || userAgent.indexOf("MSIE 9") != -1 || userAgent.indexOf("AppleWebKit") != -1 || userAgent.indexOf("Firefox") != -1) {
				return checkSilverLight('riaImg2');
		}
	}
	else {
		var mobileKeyWords = new Array('iPhone', 'iPod', 'iPad', 'BlackBerry', 'Android', 'Mobile', 'Windows CE', 'LG', 'MOT', 'SAMSUNG', 'SonyEricsson');
		for (var word in mobileKeyWords){
			if (navigator.userAgent.match(mobileKeyWords[word]) != null){
				//return popupQuickMiniForce();
				top.location.href = "http://m.cgv.co.kr/Reservation/MovieList.aspx";
				break;
			}
		}

		return checkSilverLight('riaImg1');
	}
}


var quickdata;
function QuickTicket(_areacd, _theatercd, _movie_cd, _playymd, _screencd, _starttm, _a, _b) {
	quickdata = _areacd + "|" + _theatercd + "|" + _movie_cd + "|" + _playymd + "|" + _screencd + "|" + _starttm + "|" + _a + "|" + _b;
	setQuickdataCookie("quickdata", quickdata, 1);


	if (IsMobile())
	{
		top.location.href = "http://m.cgv.co.kr/QuickReservation/";
	}
	else
	{
		location.href = "http://www.cgv.co.kr/ticket/?MOVIE_CD=" + _movie_cd + "&MOVIE_CD_GROUP=" + _movie_cd + "&PLAY_YMD=" + _playymd + "&THEATER_CD=" + _theatercd + "&PLAY_NUM=&PLAY_START_TM=" + _starttm + "&AREA_CD=" + _areacd + "&SCREEN_CD=" + _screencd;
	}
	
}

function QuickTicketEng(_areacd, _theatercd, _movie_cd, _playymd, _screencd, _starttm, _a, _b) {
    quickdata = _areacd + "|" + _theatercd + "|" + _movie_cd + "|" + _playymd + "|" + _screencd + "|" + _starttm + "|" + _a + "|" + _b;
    setQuickdataCookie("quickdata", quickdata, 1);


    if (IsMobile()) {
        top.location.href = "http://m.cgv.co.kr/QuickReservation/";
    }
    else {
        location.href = "http://www.cgv.co.kr/ticket/Eng/?MOVIE_CD=" + _movie_cd + "&MOVIE_CD_GROUP=" + _movie_cd + "&PLAY_YMD=" + _playymd + "&THEATER_CD=" + _theatercd + "&PLAY_NUM=&PLAY_START_TM=" + _starttm + "&AREA_CD=" + _areacd + "&SCREEN_CD=" + _screencd;
    }

}


function IsMobile()
{
	var IsMobiles = false;

	try {
		var mobileKeyWords = new Array('iPhone', 'iPod', 'BlackBerry', 'Android', 'Mobile', 'Windows CE', 'MOT', 'SonyEricsson');
		for (var word in mobileKeyWords){
			if (navigator.userAgent.match(mobileKeyWords[word]) != null){
				IsMobiles = true;
			}
		}
	}
	catch (ex) { }

	return IsMobiles
}


function setQuickdata(data) {
	setQuickdataCookie("quickdata", data, 1);
}

function setQuickdataCookie(name, value, expiredays) {
	var todayDate = new Date();
	todayDate.setDate(todayDate.getDate() + expiredays);
	document.cookie = name + "=" + value + "; path=/; expires=" + todayDate.toGMTString() + ";"
}

function GetQuickData() {
	var _tempQuickData = quickdata;
	quickdata = "";
	return _tempQuickData;
}

function photoTicket(booking_no, play_ymd, start_hm, movie_cd, movie_nm, reserve_qty, member_id) {

	//  alert("서비스 준비중입니다.");

	var showtime = replace(start_hm, ':', '');


	var myform = document.forms[0];

	myform.insertBefore(createHidden("reservedNumber", booking_no));
	myform.insertBefore(createHidden("showDatetime", play_ymd + showtime));
	myform.insertBefore(createHidden("movieCode", movie_cd));
	myform.insertBefore(createHidden("movieTitle", movie_nm));
	myform.insertBefore(createHidden("buyCount", reserve_qty));
	myform.insertBefore(createHidden("userid", member_id));

	var myWin = window.open("", "winName", "toolbar=0,menubar=0,scrollbars=0,status=0,resizable=0,width=1000,height=700");
	//window.open("http://cgv.phototicket.co.kr/makephototicket.php","winName","toolbar=0,menubar=0,scrollbars=0,status=0,resizable=0,width=800,height=700");

	myform.action = "http://cgv.phototicket.co.kr/makephototicket.php";
	myform.method = "post";
	myform.target = "winName";
	myform.submit();


}

function ReserveNprotect(member_id) {

	if (document.all["rsv4frame"] == undefined) {
		document.body.insertAdjacentHTML("beforeEnd", '<iframe src="http://update.nprotect.net/keycrypt/newcgv/index.html" name="rsv4frame" id="rsv4frame" width="1" height="1");"></iframe>');
	}
	//document.domain='cgv.co.kr';
}

function TicketMessage(bk_no, theaterCode) {
    var windowWidth = document.body.clientWidth; //팝업창 넓이값를 가져온다. 
    var windowHeight = document.body.clientHeight; //팝업창 높이값을 가져온다. 
    var screenWidth = window.screen.availWidth; //해상도 넓이값 
    var screenHeight = window.screen.availHeight; //해상도 높이값 
    var leftPos = (screenWidth - (windowWidth - 500));
    var topPos = (screenHeight - (windowHeight - 50));

    if (leftPos < 0) { leftPos = 0; }
    if (topPos < 0) { topPos = 0; }

    var OpenUrl = "/mycgv/diary/reserve/ria_TicketMessage.aspx?booking_No=" + bk_no + "&TheaterCode=" + theaterCode;
    var winStr = window.open(OpenUrl, "TicketMessage", "left=" + leftPos + ",top=" + topPos + ",width=490,height=307,toolbar=no,scrollbars=yes");
    winStr.focus();

}

//RIA SMS예매 전송 시 핸폰번호 변경
function SilverLightMobile(mobile1, mobile2, mobile3) {
	try {
		$.ajax({
			type: "post",
			url: "/user/join/UpdateUserInfoRia.aspx?mobile1=" + mobile1 + "&mobile2=" + mobile2 + "&mobile3=" + mobile3,
			dataType: "html",
			contentType: "application/html; charset=utf-8",
			success: function (_data) {
				//alert(_data);
			}
		});
	}
	catch (ex) {
		//alert(ex);
	}
}

function CGV_DsicountCoupon() {

	var OpenUrl = "/mycgv/diary/coupon/cgv_discount/pop_CGV_Discount_Coupon.aspx";
    window.open(OpenUrl, "DsicountCoupon", "left=0,top=0,width=672,height=520,toolbar=0,menubar=0,scrollbars=0,status=0,resizable=0");
}

function CGV_DsicountCoupon_MyCgv() {

	var OpenUrl = "/mycgv/diary/coupon/cgv_discount/list.aspx";
    window.open(OpenUrl);
}

function CJONE_DiscountCoupon_MyCgv() {

	var OpenUrl = "/mycgv/diary/coupon/cjms/list.aspx";
    window.open(OpenUrl);
}


function RIA_CardAD(LinkUrl) {
	var winStr = window.open(LinkUrl);
    winStr.focus();
}


function RealCoupon() {
    var windowWidth = document.body.clientWidth; //팝업창 넓이값를 가져온다. 
    var windowHeight = document.body.clientHeight; //팝업창 높이값을 가져온다. 
    var screenWidth = window.screen.availWidth; //해상도 넓이값 
    var screenHeight = window.screen.availHeight; //해상도 높이값 
    var leftPos = (screenWidth - (windowWidth - 500));
    var topPos = (screenHeight - (windowHeight - 50));

    if (leftPos < 0) { leftPos = 0; }
    if (topPos < 0) { topPos = 0; }

    var OpenUrl = "/popup/130419_ria_layer.html";
    var winStr = window.open(OpenUrl, "ria0419", "left=" + leftPos + ",top=" + topPos + ",width=380,height=420,toolbar=no,scrollbars=no");
    winStr.focus();

}
