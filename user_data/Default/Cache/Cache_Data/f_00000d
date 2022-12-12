;
/*
 * @name : jquery.util
 * @type : function
 * @depends : jquery.js
 */
(function( $, window, document, undefined){
	/*
	 * @name : jquery.asideMenu
	 * @desc : 지역별 극장 리스트를 json데이터에 맞춰서 배열한다.
    */
	$.fn.menuSlider = function(options) {
		var defaults = { 'transitionSpeed': 400 },
			config = $.extend(defaults , options);
			
		this.each(function(i, v) {
			var $slider = $(v),
				$btnNext = $slider.find('.btn-next'),
				$btnPrev = $slider.find('.btn-prev'),
				$scrollContent = $slider.find('div.item'),
				$scrollContentItems = $slider.find('div.item > a'),
				imgWidth = $scrollContentItems.eq(0).width(),
				totalItemCount = $scrollContentItems.length,
				visibleItemCount = 7,
				maxMove = $scrollContentItems.length - visibleItemCount,
				position = 0;

			// 내부 항목을 둘러싼 컨테이너의 너비값 지정
    		$scrollContent.css('width', totalItemCount * imgWidth);

			// 내부 항목에 on 클래스를 확인해서 화면에 표시. 기본적으로 가장 좌측에 표시가 됨.
    		for (var i = 0; i < totalItemCount; i++) {
    			if ($scrollContentItems.eq(i).hasClass('on')) {
    				position = i;
    				if (position > maxMove) position = maxMove;
    				var leftMargin = -(position * imgWidth);
    				$scrollContent.css('margin-left', leftMargin);
    				updateViewStatus(position)
    				break;
    			}
    		}

    		$btnPrev.on('click', function () {
    			position--;
    			if (position < 0) {
    				position = 0;
    			} else {
    				transition(position);
    			}
    			return false;
    		});

    		$btnNext.on('click', function () {
    			position++;
    			if (position > maxMove) {
    				position = maxMove;
    			} else {
    				transition(position);
    			}
    			return false;
    		});
			
			// position값에 따라 좌우측 이동버튼의 비활성화 상태 표시 조정.
    		function updateViewStatus(position) {
    			if (position === 0) {
    				$btnPrev.addClass('dim');
    				$btnNext.removeClass('dim');
    			} else if (position === maxMove) {
    				$btnPrev.removeClass('dim');
    				$btnNext.addClass('dim');
    			} else {
    				$btnPrev.removeClass('dim');
    				$btnNext.removeClass('dim');
    			}
    		}

			// 내부 컨텐츠 이동 애니메이션 method
    		function transition(position) {
    			var marginLeft = imgWidth * position * -1;
    			$scrollContent.animate({ 'margin-left': marginLeft }, config.transitionSpeed);
    			updateViewStatus(position);
    		}
        });
	};
	
	/*
	 * @name : jquery.asideMenu
	 * @desc : 지역별 극장 리스트를 json데이터에 맞춰서 배열한다.
    */
	$.fn.asideMenu = function(options) {
		var $aside = $(this),
            $win = $(window),
            $footer = $('.foot'),
			defaults = {isMain: false, isBricks: true, docTopMargin: 100 }, // 관람등급/가격 레이어 팝업 위치확보를 위해 최소크기 지정.
			config = $.extend(defaults , options),
            $content = $('#contents'),            
            $contentHeight = $content.height(),
            bricks = config.isBricks ? 740 : 290,
            documentTopMargin = config.isMain ? $('.head').offset().top + $('.head').height() + 10 : bricks, // 파벽유무에 따라 document 상단으로부터 무조껀 떨어져야하는 값 지정 / 메인페이지일 경우 단독 Y좌표 지정.			
			browserTopMargin = 10, // Browser 상단에서의 거리
			repeatTime = 35, // 메뉴의 현재 위치와 목표위치가 다를경우 위치를 재계산하는 빈도. 단위: 밀리세컨드.
			scrollSpeed = 1, // 메뉴가 따라오는 속도. 클수록 느려진다.
            scrolltop = (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop,
			top = scrolltop + documentTopMargin,
            bottomMargin = $(document).height() - ($footer.innerHeight() +  $aside.innerHeight()); // scrollTop 값의 최대치. 이값을 넘을 경우 사이드메뉴가 footer를 침범하기 때문에 이 값을 넘을경우 보정치를 계산해서 위치를 재조정한다.
            
		$aside.css({ 'left': getLeftPosition(), 'top': top });

		$(window).on('scroll', onWindowScrollEventHandler); 

		function onWindowScrollEventHandler(e) {

            //버튼클릭(Ajax)으로 컨텐츠 사이즈가 변경되는 경우 처리
            if($contentHeight != $content.height()) {
                //app.log($contentHeight + "/" + $content.height());                
                $contentHeight = $content.height();
                bottomMargin = $(document).height() - ($footer.innerHeight() +  $aside.innerHeight());
            }

			var startPos = parseInt($aside.css('top')),
				endPos = browserTopMargin;
            
            scrolltop = (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop;
            var scrollPosition = bottomMargin - scrolltop;

			if(scrolltop < documentTopMargin) {
				endPos = documentTopMargin - scrolltop;
			} else if(scrolltop > bottomMargin) {
                endPos = scrollPosition;
            }

			if (startPos != endPos) {
				var scrollAmount = Math.ceil(Math.abs(endPos - startPos) / scrollSpeed);
				var modifiedPosition = parseInt($aside.css('top')) + ((endPos < startPos) ? -scrollAmount : scrollAmount);
				$aside.css('top', modifiedPosition);
				timer = setTimeout(onWindowScrollEventHandler, repeatTime);
			}
		}

		
		$(window).on('resize', function () {
		    onWindowScrollEventHandler();
		    documentTopMargin = config.isMain ? $('.head').offset().top + $('.head').height() + 10 : bricks;
		    bottomMargin = $(document).height() - ($footer.innerHeight() + $aside.innerHeight());
		    $aside.css({ 'left': getLeftPosition() });
		});
		function getLeftPosition() {
			var left = $content.width() + ($content.offset()['left'] + 20);
			return left;
		}


	};



	/*
	 * @name : jquery.theaterDistrictMatrix
	 * @desc : 지역별 극장 리스트를 json데이터에 맞춰서 배열한다.
    */
	$.fn.theaterMatrix = function(options) {
		var $table = $(this),
			now = getToday(),
			defaults = { 'data':[], 'selectedDate':now, 'defaultLink':window.location.pathname, 'extraTheaterData':[] },
            config = $.extend(defaults , options);		

        var extraTheaterCount = config.extraTheaterData.length;

		// 날짜 선택이 안되있는 경우 오늘이 기준이됨.
		function getToday() {
			var now = new Date(),
				year = now.getFullYear().toString(),
				month = ("0" + now.getMonth().toString()).slice(-2),
				day = ("0" + now.getDay().toString()).slice(-2),
				today = year + month + day
			return today;
		}

		var $groupHeaderContainer = $('<ul/>');
		for(var i=0, max=config.data.length; i < max; i++) {
			var $group = $('<li/>');
			if(config.data[i]['IsSelected']) $group.addClass('on'); // 현재 지역표시 추가

			var $district = $('<a/>', {
				text: config.data[i]['RegionName'],
				href: '#'
			}).on('click', function(e) {
				var $this = $(this),
					target = $this.parent(),
					$area = $(target).children('.area').first(),
					$regions = $table.find('> ul > li');

				$regions.removeClass('on'); // 초기화
				$(target).addClass('on');

				return false;
			 }).appendTo($group);

			var theatersData = config.data[i]['AreaTheaterDetailList'];
			
			var $theaterContainer = $('<div/>', { 'class' : 'area' })
				.append(getTheaterList(theatersData, config.data[i]['RegionCode']))
				.appendTo($group);

			$groupHeaderContainer.append($group);			
		}
		$table.append($groupHeaderContainer); // 테이블에 지역/극장 리스트를 추가


		// 극장목록의 위치를 첫번째를 기준으로 조정. 
		/* 필요 없는 기능이라 제거함 181204
		var $regions = $groupHeaderContainer.children(),
			marginThreshold = $($regions[0]).offset()['left'];
		$regions.each(function(i) {
			var $this = $(this),
				leftMargin = marginThreshold - $this.offset()['left'];
			$this.find('.area').first().css('margin-left', leftMargin);
		});
		*/


		function getTheaterList(data, regionCode) {
			var $theaters = $('<ul/>'); // 지역내 극장들 리스트

			for(var i=0, max=data.length; i < max; i++) {
				var $theater = $('<li/>'), name = data[i]['TheaterName'];

				if(data[i]['IsSelected']) {
					//app.log('current theater : ' + name);
					$theater.addClass('on'); // 현재 극장표시 추가
				}
				
				url = getTheaterLink(data[i]['TheaterCode'], regionCode);
				
				var $theaterName = $('<a/>', {
					text: name,
					title: name,
					'href' : url
				}).appendTo($theater);

				$theaters.append($theater);
			}
			return $theaters;
		}

		function getTheaterLink(code, regionCode) {
			var params = $.param({ 
					'areacode' : regionCode,
					'theaterCode' : code,
					'date' : config.selectedDate
				}),
				url = config.defaultLink + '?' + params;
			
			// 예외데이터가 있는 경우에만 아래 구문을 수행
			if(~~extraTheaterCount != false) { 
				var params = $.param({ 'theaterCode' : code });
				for (var j=0, max=config.extraTheaterData.length; j < max; j++) {
				 	if(config.extraTheaterData[j]['code'] === code) {
				 		//url = config.extraTheaterData[j]['link'] + '?' + params;
                        url = config.extraTheaterData[j]['link'];
				 		config.extraTheaterData.splice(j,1); // 링크가 추가되면 예외데이터 array에서 제거
				 		extraTheaterCount--; // 남아있는 예외데이터의 수를 조정, 0이되면 예외데이터 확인을 수행하지 않는다.
				 		break;
				 	}
				}
			}

			return url;
		}
	};


	/*
	 * @name : jquery.sameHeightFrame
	 * @desc : iframe 높이를 컨텐츠 높이만큼 지정하되 최소값보다 작으면 최소값을 지정.
	 * @function : resize - 외부에서 호출가능한 높이재산정 method. iframe내부 document에서 load될때 실행한다.
    */
	$.fn.sameHeightFrame = function(options) {
		var $frame = $(this),
			defaults = { 'minHeight':100 }, // 관람등급/가격 레이어 팝업 위치확보를 위해 최소크기 지정. (최소사이즈 100으로 수정)
            config = $.extend(defaults , options),
            options = options;

        // add circle progress before load contents
		var $loader =  $('<div/>').addClass('preloading').css({'height': '300px', 'position':'relative'});
        $frame.before($loader);
        app.loading().show({ 'target': $loader, 'circleType':'large' });

		/* change iFrame Height to document height */
		function frameResize(options) {
			$frame.css({"height": config.minHeight}); // 갱신시 높이 재산정을 위해 최소높이로 임시 조정.
    		var h = $frame.contents().height();
    		$frame.css({"min-height": config.minHeight, "height":h});
    		//app.log('iframe height is changed to ' + h);

    		// remove circle progress after load contents
    		$loader.remove();
            if(config.callback)
            {
                if(typeof config.callback == 'function') 
                    config.callback();
            }
                
    	};
        

		return {
			resize: frameResize
		};
	};


	/*
	 * @name : jquery.like
	 * @desc : 
     * ToDo : 
    */
    $.fn.like = function (options) {        
        var likeType = { 'star':'star', 'heart':'heart' },
			fMovies = [],
			userFavoriteMovieData = {},
            defaults = { },
            config = $.extend(defaults , options);


        if(window.userFavoriteMovie) {
        	userFavoriteMovieData =  window.userFavoriteMovie;
        	for(var i=0, max = userFavoriteMovieData.length; i < max; i++) {
				fMovies.push(userFavoriteMovieData[i].toString());
			}
		}


		/*
		* @name : 
		* @desc : get first index which match with target value from target array
		* @param : array - target array, value - target value
		*/
		function getArrayIndex(array, value) {
			for(var i=0; i<array.length; i++) {
				if(value === array[i]) return i;
			}
		}

        return this.each( function (i, v) {
			var $like = $(v),
				val = $like.val(),
				likeCount = $like.next().find('i:first'),
				isLogin = app.config('isLogin');


			if(getArrayIndex(fMovies, val) > -1 && isLogin) {
				$like.addClass('on');
			}

			$like.on("click", onLikeButtonClickEventHandler);

			function onLikeButtonClickEventHandler(e) {				
				var $this = $(this),
					isChecked = $this.hasClass('on');
				if ((!$this) || !val) return;
				if (!isLogin) { 
					app.goLogin(); 
					return false;
				}
				isChecked ? RemoveFavoriteMovie() : AddFavoriteMovie();
				return false;
			}

			function AddFavoriteMovie() {
				//$like.off("click");

				var data = "{ movieIdx : " + val.toString() + "}";
				app.ajax().set({
					dataType: 'json',
                    url: '/common/ajax/movies.aspx/AddFavoriteMovie',
                    contentType: "application/json; charset=utf-8",
                    data: data,
                    successHandler: function (result) {
                        switch (result.resultCode) {
                            case "1":
                                likeCount.text(result.resultData); // set like total count on right side of like button.

                                $like.addClass("on");
                                if(confirm("위시리스트에 등록되었습니다.\n위시리스트로 이동하시겠습니까?")) {
                                    top.location.href = "/user/movielog/";
                                }
                                break;
                            case "-1":
                                app.goLogin();
                                break;
                            case "-2":      //data 존재 안함
                                location.reload();
                                break;
                            default:
                                alert("장애가 발생하였습니다. 잠시 후 다시 시도해 주세요.");
                                break;

                        }
                    }
                });
			}

			/*
			* @name : 
			* @desc : call removefavorite api 
			* ToDo : make remove api
			*/
			function RemoveFavoriteMovie() {
				//$like.on("click");

				var data = "{ movieIdx : " + val.toString() + "}";
				app.ajax().set({
					dataType: 'json',
                    url: '/common/ajax/movies.aspx/RemoveFavoriteMovie',
                    contentType: "application/json; charset=utf-8",
                    data: data,
                    successHandler: function (result) {

                        switch (result.resultCode) {
                            case "1":
                                likeCount.text(result.resultData); // set like total count on right side of like button.
                                $like.removeClass("on");
							    alert("'위시리스트'에서 삭제되었습니다.");
                                break;
                            case "-1":
                                location.reload();
                                break;
                            case "-2":
                                app.goLogin();
                                break;
                            default:
                                alert("장애가 발생하였습니다. 잠시 후 다시 시도해 주세요.");
                                break;
                        }
                    }
                });

			}
        });
    };

    /*
	 * @name : jquery.rangeSlider
    */
    $.fn.rangeSlider = function (options) {
        var nowYear = new Date().getFullYear(),
            min = 1950,
            max = 2030,
            range = max - min,
            cStart = options.start.val() || 2000, cEnd = options.end.val() || nowYear,
            defaults = {
                'sliderOptions' : {
                    'range': true,
                    'min' : min,
                    'max' : max,
                    'values': [cStart, cEnd]
                }
            },
            config = $.extend(true, defaults , options);

        return this.each(function(i, v){
            var $item, slider;
            if (typeof $.fn.slider == 'function') {
                $item = $(v);
                
                config.sliderOptions.slide = function (event, ui) {
                    config.start.val(ui.values[0]);
                    config.end.val(ui.values[1]);
                };
                slider = $item.slider(config.sliderOptions);
                config.start.val($item.slider("values", 0)).on('change', changeStartValueHandler);
                config.end.val($item.slider("values", 1)).on('change', changeEndValueHandler);
            }

            function changeStartValueHandler(){
                var insertValue = config.start.val();
                if(isNaN(insertValue)){
//                    alert('숫자만 입력가능합니다.');
//                    config.start.val(cStart);
                    return false;
                }
                insertValue = parseInt(insertValue, 10);
                if(insertValue < min || insertValue > cEnd){
//                    alert('입력가능한 범위가 아닙니다.');
//                    config.start.val(cStart);
                    return false;
                }
                cStart = insertValue;
                setSliderValue();
            }

            function changeEndValueHandler(type){
                var insertValue = config.end.val();
                if(isNaN(insertValue)){
//                    alert('숫자만 입력가능합니다.');
//                    config.end.val(cEnd);
                    return false;
                }
                insertValue = parseInt(insertValue, 10);
                if(insertValue > max || insertValue < cStart){
//                    alert('입력가능한 범위가 아닙니다.');
//                    config.end.val(cEnd);
                    return false;
                }
                cEnd = insertValue;
                setSliderValue();
            }

            function setSliderValue(){
                if(slider){
                    slider.slider('values', [cStart, cEnd]);
                }
            }
        });
    };




	

    /*
	 * @name : jquery.tile
	 * @desc : 하위 아이템들을 높이와 컬럼수에 맞춰서 재배치한다.
	*/
	$.fn.tile = function (options) {
		var $this = $(this),
			defaults = {
				'column' : 2,
				'itemMargin' : 10,
				'listHeights' : [],
				'leftMargins' : [],
				'targetClass' : 'box-round'
			},
			config = $.extend(defaults, options);

		$tiles = $this.find('.'+config.targetClass);
		var itemWidth = $tiles.first().width();

		if(config.listHeights.length === 0) {
			for(var i=0; i<config.column; i++) {
				config.listHeights.push(0);
			}
		}

		if(config.leftMargins.length === 0) {
			for(var i=0; i<config.column; i++) {
				var left = (i === 0) ? 0 : (itemWidth + config.itemMargin)*i;
				config.leftMargins.push(left);
			}
		}

		//app.log(config.leftMargins);

		function getArrayIndex(array, value) {
			for(var i=0; i<array.length; i++) {
				if(value === array[i]) return i;
			}
		}

		$tiles.each(function(i) {
			var $this = $(this),
				height = $this.innerHeight(),
				minVal = Math.min.apply(Math, config.listHeights),
				columnNum = getArrayIndex(config.listHeights, minVal);
				
			$this.css({ 
				"position" : "absolute", 
				"top" : function() { return config.listHeights[columnNum]; },
				"left" : function() { return config.leftMargins[columnNum]; }
			});

			//app.log(config.listHeights[columnNum] + '+' + height + '+' + config.itemMargin);
			
			config.listHeights[columnNum] = config.listHeights[columnNum] + height + config.itemMargin; // update list height list as current value;
		});

		// set container height after adding items.
		$this.css("min-height", function() {
			return Math.max.apply(Math, config.listHeights);
		});
	};

	


    /*
	 * @name : jquery.tileGallery
	 * @desc : default column : 3, 
	*/
	$.fn.tileGallery = function (options) {
		var defaults = {
				'type' : 'general', // 'general', 'event', 'none' <= 수동 클릭 설정
				'data' : [],
				'listHeights' : [0,0,0],
				'leftMargins' : [0,270,540],
				'imageMargin' : 10,
				'limit' : 20,
				'imageWidth' : 260,
                'callback' : null       //item 1개씩 추가 후 event
			},
			config = $.extend(defaults, options);


		return this.each(function(i, v) {
			var $this = $(v),
				$win = $(window),
				$moreButton = $("#btnMoreData"),
				maxItemCount = 0,
				imagesListPointer = 0,                
				totalImagesCount = config.data.length,
				loadedItems = new Array(totalImagesCount),
				loadedItemsCount = 0,
				bottomMargin = -10;


			// 데이터가 선언되지 않은채 넘어왔을 경우, 빈데이터 형식으로 초기화.
			if(totalImagesCount === undefined) {
				//app.log('current data is undefined. data length will be 0.');
				config.data = [];
				totalImagesCount = 0;
			}
			
			
			// 데이터가 없을 경우 처리
			if(totalImagesCount === 0) {
				//app.log('data length is 0. morebutton will be hide and no image text will be appear.');
				//$this.text('No Images'); // ToDo:데이터 없을 경우 페이지 렌더링 처리는 이곳에 추가.
				$moreButton.hide(); 
			} else {
				$this.on("LoadMoreItemEvent", onLoadMoreItemEventHandler);	
			}

			/*
			* image load event handler           
			* @type : EVENT
			*/
			function onLoadMoreItemEventHandler(e) {
				app.loading().show(5); // show progress while loading images.

				imagesListPointer = maxItemCount;
				maxItemCount = maxItemCount + config.limit;

				// break loading image process 
				if(maxItemCount >= totalImagesCount) {
					maxItemCount = totalImagesCount;
					$this.off("LoadMoreItemEvent");
					//app.log('every items are loaded complete.');
					$moreButton.hide(); // hide button when it doesn't necessary. ex.) total image count is under 20.
				}
				
				

				for (var i=imagesListPointer; i < maxItemCount; i++) {	
					var tempImg = new Image();
					tempImg.index = i;
					
					tempImg.onload = function() {
                        //app.log("로드됐어~:" + this.src);
                        //app.log("몇번?::::" + this.index);
						addToLoadedItems(this);
					};
					tempImg.onerror = function(e){
                        //app.log("ON ERROR 이미지야! 몇번?::::" + this.index);
						addToLoadedItems(this, e);
					};

                    tempImg.src = config.data[i]['imageUrl'];
				}
			}
			

			/*
			* input item from tempImg attr to loadedItems
			*
			* @param {Image()} _this : image object has a source, index
			* @param {object} it will added when loading fail.
			*/
			function addToLoadedItems(_this, error) {
				var item = {}, url = _this.src,  alt = '', w = _this.width, h = _this.height, index = _this.index, 
                    link='', errorImage = {};
                
				if(config.data[index]['description']) {
					alt = config.data[index]['description'];
				}
				item = { "index": index, "url": url, "width": w, "height": h, "alt":alt };

				if(error) {
					if(config.type === 'event') {
						errorImage = { "url": window._NO_IMAGE.landscape, "link":"#", "width":config.imageWidth, "height":150, "alt":"default error image" };
					} else {
						errorImage = { "url": window._NO_IMAGE.square, "link":"#", "width":config.imageWidth, "height":config.imageWidth, "alt":"default error image" };
					}
					item = $.extend(item, errorImage);
				}

				if(config.type === 'event') { // event type need more property
					item = $.extend(item, {"link": config.data[index]['link'], "target": config.data[index]['target'] || ''});  // add link, target to item

					var reverseStopPoint = totalImagesCount - (totalImagesCount%3);
					if(index >= reverseStopPoint) {
						index = index;
					} else {
						var indexThreshold = index % 3;
						if(indexThreshold == 0) {
							index = index + 2;
						} else if(indexThreshold == 2) {
							index = index - 2;
						} else {
							index = index;
						}
					}
				}

				loadedItems[index] = item;
				loadedItemsCount++; // @ triggerAddItem

				triggerAddItem();
			}

			/*
			* @ onLoadMoreItemEventHandler
			* start AddItemEvent after every image loaded complete.
			*/
			function triggerAddItem(){
				if (maxItemCount == loadedItemsCount) {
					$this.trigger("AddItemEvent");
				}
			}

			/*
			* add image to list event. triggered after load images.
			* @type : EVENT
			*/
			$this.on("AddItemEvent", onAddItemEventHandler);
			function onAddItemEventHandler(e) {	
				if(maxItemCount > totalImagesCount) {
					$this.off("LoadMoreImageEvent"); // unbind load event after every images loaded complete.
				}
				
				for (var i=imagesListPointer; i < maxItemCount; i++) {
					addItemToContainer(loadedItems[i]);				
				}

				setContainerHeight();

				// add item count text to more button while existing
				if($moreButton.is(':hidden') === false) {
					$moreButton.find("em").text(maxItemCount);
					$moreButton.find("i").text(totalImagesCount);
					//$this.find("div").eq(imagesListPointer).find("a").focus(); //(이 포커스 때문에 스크롤 움직임!)
				} else {
					$this.trigger("LoadMoreItemEvent");
					//$this.find("div").eq(config.limit).find("a").focus(); // 나머지 전체로딩으로 변경됨에 따라 추가로딩된 첫번째 아이템에 focus가 가도록 변경. (이 포커스 때문에 스크롤 움직임!)
				}

				app.loading().hide(); // hide progress after finishing add images.

                
                //아이템 추가 후 호출할 event있는지 check
                if (typeof config.callback == 'function') {
                    config.callback(config.data);
                }
			}


			function getArrayIndex(array, value) {
				for(var i=0; i<array.length; i++) {
					if(value === array[i]) return i;
				}
			}

			/* 
			* @ onAddItemEventHandler
			* set container height
			*/
			function setContainerHeight() {
				// event has a different bottom margin because of image that right bottom corner in background
				if(config.type === 'event') {
					var maxVal = Math.max.apply(Math, config.listHeights),
						margins = [16,64,156],
						index = getArrayIndex(config.listHeights, maxVal);
					bottomMargin = margins[index];
				}

				// set container height after adding items.
				$this.css("min-height", function() {		        	
					return Math.max.apply(Math, config.listHeights) + bottomMargin;
				});
			}

			function addItemToContainer(target) {
				var url = target['url'], 
					index = target['index'], 
					alt = target['alt'],
					minVal = Math.min.apply(Math, config.listHeights),
					columnNum = getArrayIndex(config.listHeights, minVal),
					height = Math.round(target['height'] / target['width'] * config.imageWidth),					
					$returnValue = $('<div><a id="tile_' + index + '" href="#"></a></div>'),
					$a = $returnValue.find("a").filter(":first");   

				switch(config.type) {
					case 'event':
						var link = target['link'], linkTarget = target['target'];
						$a.attr("href", link);
						$a.attr("target", linkTarget);
						break;
                    case 'none':
                        break;
					case 'general':
						// Same as Default
					default:
						$a.on("click", function(e) {
                            //app.log('## click');
							e.preventDefault();
							app.instWin.add({'type': 'photo', 'data' : config.data, 'offset': index, 'more' : loadMoreItem, 'mask' : true});
							return false;
						});
						break;
				}

				//$a.append('<img src="' + url + '"style="height:' + height + 'px;" alt="' + alt + '" onerror="errorImage(this,{type:"square"})" />');
                $('<img>').attr({'src': url, 'alt' : alt}).css({'height': height}).on('error', function (e) {errorImage(this,{type:'square'});}).appendTo($a);
				
				$returnValue.css({ 
					"position" : "absolute", 
					"top" : function() { return config.listHeights[columnNum]; },
					"left" : function() { return config.leftMargins[columnNum]; }
				});
				
				config.listHeights[columnNum] = config.listHeights[columnNum] + height + config.imageMargin; // update list height list as current value;

				$returnValue.data("index", target['index']);
				$this.append($returnValue); 
			}


			/* Get More itmes */
			// click : load more image
			
			$moreButton.on("click", loadMoreItem);

			function loadMoreItem() {
				$this.trigger("LoadMoreItemEvent");

				if(config.type === 'general') {
					$moreButton.hide();  // morebtn will be show every limit in event
				}
			}

			// start load item event at first time.
			$this.trigger("LoadMoreItemEvent");

		 });
	};

	/*
	 * @name : jquery.point
	 * @desc : default type / star, set event handler, renderer.
     * ToDo : 읽어들이는 점수 validate
    */
    $.fn.point = function (options, pointSetValue) {   //2014.12 평점UI개선 : pointSetValue 인자 추가
		var thisPointSetValue = 10; //2014.12 평점UI개선 : 추가
		
		//2014.12 평점UI개선 : 추가
		if(pointSetValue != "undefined" && pointSetValue > 0) {
			thisPointSetValue = pointSetValue;
		}

        var pointType = { 'star':'star', 'heart':'heart' },
            rendererType = { 'view' : 'view', 'write' : 'write' },
            pointNum = thisPointSetValue,	//2014.12 평점UI개선 : 수정
			writePoint = pointNum,
            defaults = {
                'type' : 'star', 'renderer' : 'view'
            },
            config = $.extend(defaults , options);
		
		this.each(function(i, v){
			var point = 0, 
				$point = $(v), 
				$em = $(v).find('em'), 
				data = $point.data();

			// rendering이 1회만 발생하도록 하기 위한 방어코드 flag 
			$point.find('span').remove();
            
			if(config.renderer == 'write') {   
				point = pointNum;
				$em.before(write(point));
				$em.text(point).append($('<span class="hidden">점/10점 만점</span>'));
			} else {
				point = $point.find('>em').text();
				$em.before(view(point));
				setPointText(point);
			}

			function view(score) {
				var renderTemplate = [
					'<span class="point-off">',
						'<span class="point-on" style="width: ' + (score*10) + '%"></span>',
					'</span>'
				].join('');
				return renderTemplate;
			}

			function write(score) {
				var $temp = $('<div/>'), pointNum=score;

				for (var i=1; i<11; i++) {
					var position = (i%2) ? 'left' : 'right',
						txt =  i + '점';
					$item = $('<button/>', { 'type': 'button', 'title': txt, 'text': txt }).addClass(position).appendTo($temp);
				}

				function setPoint(score) {
					$buttons.removeClass('on');
					for(var i=0; i < score; i++) {
						$($buttons[i]).addClass('on');
					}
				}

				var $buttons = $temp.find('button');

				$buttons.on('mouseover', function() {
					var score = $(this).index() + 1;
					setPoint(score);
				});

				$buttons.on('mouseout', function() {
					setPoint(pointNum);
				});

				$buttons.on('click', function() {
					writePoint = pointNum = $(this).index() + 1; // 점수지정
					setPoint(pointNum);
					setPointText(pointNum);
				});

				setPointText(pointNum); // 점수초기화
				setPoint(pointNum);

				return $buttons;
			}

			// 점수표시 method
			function setPointText(score) {
				$em.text(score);
				$em.append($('<span>' + score + '점/10점 만점</span>'));
			}

			$point.data("rendered","rendered");
		});
		var _this = this;
		if(config.renderer == 'write') {
			_this = {
        		'getPoint': function () { return writePoint; }
    		}
		}

        return _this;

    };
    /*
	 * @name : jquery.editor
     * @depends : ckeditor.
	 * @desc : editor wrapper 함수
     toolbar : [
                    { name: 'document', groups: [ 'mode', 'document', 'doctools' ], items: [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ] },
	                { name: 'clipboard', groups: [ 'clipboard', 'undo' ], items: [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
	                { name: 'editing', groups: [ 'find', 'selection', 'spellchecker' ], items: [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
	                { name: 'forms', items: [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ] },
	                '/',
	                { name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ], items: [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ] },
	                { name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi' ], items: [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ] },
	                { name: 'links', items: [ 'Link', 'Unlink', 'Anchor' ] },
	                { name: 'insert', items: [ 'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ] },
	                '/',
	                { name: 'styles', items: [ 'Styles', 'Format', 'Font', 'FontSize' ] },
	                { name: 'colors', items: [ 'TextColor', 'BGColor' ] },
	                { name: 'tools', items: [ 'Maximize', 'ShowBlocks' ] },
	                { name: 'others', items: [ '-' ] },
	                { name: 'about', items: [ 'About' ] }
                ]
                enterMode, shiftEnterMode : default > ENTER_P, ENTER_BR, ENTER_DIV
	 */
    $.fn.editor = function (options){
        check();
        var defaults = {
                toolbar : [
                    { items: [ 'Source', 'Undo', 'Redo'] },
                    { items: [ 'FontSize', 'TextColor', 'BGColor' ] },
                    { items: [ 'Bold', 'Italic', 'Underline', 'Strike' ] },
                    { items: [ 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'list','indent', 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent' ] },
	                { items: [ 'Image', 'Link', 'Unlink', 'Table', 'HorizontalRule' ] },
                    { name: 'about', items: [ 'About' ] }
                ],
                enterMode : CKEDITOR.ENTER_BR,
                explain : ''
            },
            config = $.extend(true, defaults , options);
        
        function check(){
            if(!window.CKEDITOR) $.error('not defined CKEDITOR.');
        }

        return this.each(function(i, v){
            var $v = $(v), text = $v.val();
            $v.before('<p class="hidden">CK Editor 단축키 설명 * Esc Key: 에디터의 레이어 팝업을 닫는다., * Enter Key : </p>').ckeditor({
                toolbar: config.toolbar,
                enterMode : config.enterMode
            }).val(text);
        });
    };

    /*
	 * @name : jquery.naverMap
     * @depends : naver map api.
	 * @desc : naver map wrapper 함수
	 */
    $.fn.naverMap = function (options){
        var defaults = {w:978, h:448},
            config = $.extend(true, defaults , options);
        
        if (!config.code || (config.data && !config.data.length)) $.error('not defined default data.');
        var theater = config.data.filter(function (v, i, a) {
                return v.code == config.code;
            })[0];

        //if(!window.nhn) $.error('not defined nhn.');
        if(!theater || !theater.code) $.error('not defined theater info.');

        var target = $(this)[0], theaterPoint, oMap, oMapTypeBtn, oIcon, iconSize, iconOffset, oMarker, oLabel;
            
        // init Point.
        theaterPoint = new naver.maps.LatLng(theater.lat, theater.lng);
        // init Map.
          oMap = new naver.maps.Map('map', {
                        center : new naver.maps.LatLng(theater.lat, theater.lng),
                        size : new naver.maps.Size(config.w, config.h),
                        draggable : false
                    });


        // init All Theater Marker.
        config.data.forEach(function(v, i, a){
          //  oMarker = new nhn.api.map.Marker(oIcon, { title: v.label });

            var T_title = v.label;
             var markerOptions = {
              position: new naver.maps.LatLng(v.lat, v.lng).destinationPoint(45, 7),
		        map: oMap,
		     //   title : v.label,
                icon: {
		            url: 'http://img.cgv.co.kr/theater/pin_spot2.png',
		            size: new naver.maps.Size(28, 37),
		            origin: new naver.maps.Point(0, 0),
		            anchor: new naver.maps.Point(14, 37)
		        }
		    };
          //  markerOptions.setTitle(title);
		    oMarker = new naver.maps.Marker(markerOptions);
            oMarker.setTitle(T_title);



//              var contentString = [
//    '<div class="iw_inner"  style="height:15px;width:300px">',
//    '<span align="center"><b> '+T_title+' </b></span>',
//    '</div>'
//].join('');

//		   

//		    var infowindow = new naver.maps.InfoWindow({

//		        content: contentString,

//		        maxWidth: 140,
//		        backgroundColor: "#ffffff",
//		        //borderColor: "#2db400",
//		        borderColor: "#000",
//                borderWidth: 2,
//                anchorSize: new naver.maps.Size(7, 7),
//		        anchorSkew: true,
//		        anchorColor: "#eee",

//		        //pixelOffset: new naver.maps.Point(20, -20)
//		    });


//		    naver.maps.Event.addListener(oMarker, "click", function (e) {
//		        if (infowindow.getMap()) {
//		            infowindow.close();
//		        } else {
//		            infowindow.open(oMap, oMarker);
//		        }
//		    });

        });

    };
    //
    /*
	 * @name : jquery.visualMotion
     * @depends : jquery.
	 * @desc : visual motion. 
     * @desc : indicator 사이 간격 margin - BTN_MARGIN = 5
     * @desc : indicator button width 사이즈 - BTN_WIDTH = 13
     // TODO : 성능이슈 발생시, 이미지 처리방식 변경.
     // TODO : motion index 에 대한 queue 처리. > motion_queue.
     // TODO : 모션 방향 처리 : 좌 > 우, 우 > 좌
     // TODO : type 을 추가한다. banner, photo
     // TODO : 비동기 데이타 처리 관련 추가?
	 */
    $.fn.visualMotion = function (options){
        var BTN_MARGIN = 5, BTN_WIDTH = 13, BTN_SIZE = BTN_MARGIN + BTN_WIDTH,
            START_INDEX = 0,
            isMotioning = false,
            defaults = {
                'duration'  : 500,
                'term'      : 4000,
                'offset'    : START_INDEX,
                'roof'      : true,
                'auto'      : false,
                'fill'      : true,
                'effect'    : 'none',       //'fade', 'slide', 'none'
                'type'      : 'banner'      //'banner', 'photo, 'date'
            },
            config = $.extend(true, defaults , options);
        
        var $wrap = $(this[0]), $area = $wrap.parent(), w = $area.width(), h = $area.height(), r = w/h,
            $arrow = $wrap.find('button.btn-prev , button.btn-next'), $control = $wrap.find('button.btn-play, button.btn-pause'),
            $itemWraps = $wrap.find('>.item-wrap'), len = $itemWraps.length,
            startLeft = parseInt( (w - (((len + 1) * BTN_WIDTH) + (len * BTN_MARGIN)))/2),  
            timer, cIndex = config.offset, motion_queue = [];

        // init
        $itemWraps.each(function(i, v){
            var $itemWrap = $(v), $item = $itemWrap.find('>.item'), $indicator = $itemWrap.find('>button');
                
            if(i != cIndex){
                $item.css({'width':w, 'height':h, 'display':'none'});
                unActiveLink($item);
            } else {
                $item.css({'width':w, 'height':h});
                $indicator.addClass('on').attr('title', '선택');    
            }

            if(config.type === 'banner'){
                $item.find('img').css({'width' : '100%', 'height' : '100%'});
            }
        });

        //app.log('visual Motion > config.type : ' + config.type + ', ' + cIndex);
        if(config.type === 'photo') {
            preLoadImage(cIndex);
        }

        // arrow button
        $arrow.on('click', function (e) { 
            //app.log('e: click arrow' + isMotioning);
            if(isMotioning) return;
            
            
            var $arrowBtn = $(this);
            //app.log($arrowBtn);
            
            if($arrowBtn.hasClass('dim')) return;

            isMotioning = true;
            

            pause();
            mIndex = $arrowBtn.hasClass('btn-prev') ? -1 : 1;
            move(getIndex(mIndex));
        });

        if(!config.roof){
            //app.log('## config.roof');
            setArrow(cIndex);
        }

        config.auto && play();

        // play, pause control
        $control.css({'left' : startLeft + (len * BTN_SIZE), 'display' : 'block'}).on('click', function (){
            //app.log('e: click control');
            if($control.hasClass('btn-pause')){ // do pause
                pause();
            } else { // do play
                play();
            }
            return false;
        });

        // set indicator.
        $itemWraps.find('> button').each(function(i, v){
            var $b = $(v), left = startLeft + (BTN_SIZE * i);
            $b.css({left: left, 'display' : 'block'}).data('index', i);
        }).on('click', function () {
            //app.log('e: click indicator');
            var sIndex = $(this).data('index');         // select indicator index.
            if(isMotioning || cIndex === sIndex) return;
            isMotioning = true;
            pause();
            move(sIndex);
        });

        function preLoadImage (_index) {
            loadImage($itemWraps.eq(cIndex).find('img'));
            loadImage($itemWraps.eq(getIndex(1)).find('img'));
            loadImage($itemWraps.eq(getIndex(-1)).find('img'));

            function loadImage (_$img) {

                if(!_$img.length) return;
                var img = _$img[0], src = '', tempImage = new Image(), src = _$img.data('src');

                if(!img.src){
                    tempImage.onload = function () {
                        //app.log('src : ' + this.src + ', w : ' + this.width + ', h : ' + this.height);
                        var imgW = this.width, imgH = this.height, imgR = imgW/imgH;

                        if(r > imgR){
                            if(h < imgH) {
                                _$img.css({'height': '100%'});
                            } else {
                                _$img.css({'margin-top': (h - imgH) / 2});
                            }
                        } else {
                            if(w < imgW) {
                                _$img.css({'width': '100%', 'margin-top': (h - parseInt(w / imgR, 10)) / 2});
                            } else {
                                _$img.css({'margin-top': (h - imgH) / 2 + 'px'});
                            }
                        }
                        _$img.attr('src', src);
                    };
                    tempImage.src = src;
                }
            }
        }

        // a : remove attribute href, iframe : remove attribute src
        function unActiveLink($t) {
            if(!$t.length) return;
            var tag = $t[0].tagName;
            if(tag == 'A'){
                $t.data('href', $t.attr('href')).removeAttr('href');
            } else {
                $t.data('src', $t.attr('src')).removeAttr('src');
                $t.attr('src', $t.data('src'));
            }
        }

        function activeLink($t) {
            $t.attr('href', $t.data('href'));
        }

        function getIndex(m){
            var move = cIndex + m, min = 0, max = len - 1;
            if(move < min){
                move = max;
            } else if(move >= len) {
                move = min;
            }
            return move;
        }

        function play() {
            //app.log('## do play');
            if($control.hasClass('btn-play')){
                $control.removeClass('btn-play').addClass('btn-pause').text('일시멈춤');
                if(config.auto){
                    config.auto = false;
                } else {
                    move(getIndex(1));
                }
                timer = setInterval(function (){
				    move(getIndex(1));
                    if(!config.roof && getIndex(1) === (len - 1)){
                        //app.log('## setInterval pause');
                        pause();
                        return;
                    }
			    }, config.duration + config.term);
            }
        }

        function pause() {
            clearInterval(timer);
            if($control.hasClass('btn-pause')){
                //app.log('## do pause');
                $control.removeClass('btn-pause').addClass('btn-play').text('자동 넘기기 시작');
            }
        }

        function move(_moveIndex){
            doBefore(_moveIndex);
            $itemWraps.find('>button').removeClass('on').removeAttr('title').eq(_moveIndex).addClass('on').attr('title', '선택됨.');    // active indicator.
            var exec = function () {};
            switch (config.effect){
                case 'fade' : exec = fade; break;
                case 'slide' : exec = slide; break;
                default : exec = noneEffect; break;
            }
            exec(_moveIndex);
            if(config.type === 'photo') {
                preLoadImage(_moveIndex);
            }
        }

        function noneEffect (_moveIndex) {
            var $nli = $itemWraps.eq(_moveIndex);
            $itemWraps.eq(cIndex).find('.item').hide();
            $nli.addClass('move').find('.item').show(0, function(){
                unActiveLink($itemWraps.eq(cIndex).find('.item'));
                activeLink($nli.find('.item'));
                cIndex = _moveIndex;
                $itemWraps.removeClass('on').not(':eq(' + cIndex + ')').find('.item').hide();
                $nli.removeClass('move').addClass('on');
                isMotioning = false;
                doCallback();
            });
            $wrap.data('index', _moveIndex);
        }

        function fade(_moveIndex){
            var $nli = $itemWraps.eq(_moveIndex);
            $nli.addClass('move').find('.item').fadeIn(500, function(){
                unActiveLink($itemWraps.eq(cIndex).find('.item'));
                activeLink($nli.find('.item'));
                cIndex = _moveIndex;
                $itemWraps.removeClass('on').not(':eq(' + cIndex + ')').find('.item').hide();
                $nli.removeClass('move').addClass('on');
                isMotioning = false;
                doCallback();
            });
            $wrap.data('index', _moveIndex);
        }

        function slide (_moveIndex) {
            var $nli = $itemWraps.eq(_moveIndex);
            $nli.addClass('move').find('.item').css({'left': w});   // 좌/우 방향 컨트롤 위치.
            $itemWraps.filter(function(i, v){return i == cIndex || i == _moveIndex;}).find('>.item').animate({left : '-=' + w, easing : 'easeOutQuart'}, config.duration, function (){
                unActiveLink($itemWraps.eq(cIndex).find('.item'));
                activeLink($nli.find('.item'));
                cIndex = _moveIndex;
                $itemWraps.removeClass('on');
                $nli.removeClass('move').addClass('on');
                isMotioning = false;
                doCallback();
            });
            $wrap.data('index', _moveIndex);
        }

        function setArrow (_moveIndex) {

            var $prev = $arrow.first(), $next = $arrow.last();
            if(_moveIndex === 0){
                $prev.addClass('dim');
                $next.removeClass('dim');
            } else if (_moveIndex === (len - 1)){
                $prev.removeClass('dim');
                $next.addClass('dim');
            } else {
                $prev.removeClass('dim');
                $next.removeClass('dim');
            }
        }

        function doBefore(_moveIndex){
            config.onBeforeHandler && config.onBeforeHandler(_moveIndex);
            if(!config.roof){
                setArrow(_moveIndex);
            }
        }

        function doCallback(){
            config.callback && config.callback(cIndex);
        }

        return {'pause' : pause};
    };
    /*
	 * @name : jquery.graphChart
     * @depends : jquery.jqplot
	 * @desc : jqplot 차트 wrapper
	 */
    $.fn.graphChart = function (options){
        
        if(!options.data || options.data.length === 0 ) return this;    //데이타가 없는 경우, 예외 표기할 수 있는 위치.
        var htmlBackgroundColor = $('html').css('background-color'),
            defaults = {
                animate: !$.jqplot.use_excanvas,// Only animate if we're not using excanvas (not in IE 7 or IE 8)..
                grid: {
                    drawGridLines: false,        // wether to draw lines across the grid or not.
                    gridLineColor: htmlBackgroundColor,    // *Color of the grid lines. , 999999
                    background: htmlBackgroundColor,      // CSS color spec for background color of grid., fffdf6, fdfcf0
                    borderColor: htmlBackgroundColor,     // CSS color spec for border around grid., 999999, fdfcf0
                    shadow: false               // draw a shadow for grid.
                },
                axesDefaults : {
                    tickOptions : {fontSize : '12px'}
                }
            },
            type = options.type || 'bar',
            chartInfo = {
                'bar' : {
	                seriesDefaults: {
	                    renderer: $.jqplot.BarRenderer,
                        marginTop : '20px',
	                    rendererOptions: {
                            padding : 50,
                            barPadding : 50,
                            barMargin : 50,
	                        varyBarColor: true,
                            highlightMouseOver : false,
                            barWidth : 30,
                            marginBottom : 20
	                    }
	                },
	                axes: {
	                    xaxis: {
	                        renderer: $.jqplot.CategoryAxisRenderer,
                            rendererOptions : {fontSize : '12px'},
                            labelOptions : {fontSize : '12px'},
                            tickOptions : {formatString: "%s", fontSize : '12px' }
	                    },
	                    yaxis: {show: false, showTicks : false, tickOptions : {formatString: "%s", fontSize : '12px' }}
	                }
	            },
                'line' : {
	                seriesDefaults: {
	                    showMarker:true,
                        rendererOptions : {padding: 10, fontSize : '12px'}
	                },
	                axes: {
	                    xaxis: {
	                        show: false,
	                        renderer: $.jqplot.CategoryAxisRenderer,
                            rendererOptions : {padding: 10},
                            labelOptions : {fontSize : '12px'}
	                    },
	                    yaxis: {show: false, max: 12, min : -1, showTicks : false, tickOptions : {formatString: "%s"}}
	                },
                    seriesColors : ['#41556c', '#d13867']
	            },
                'donut' : {
                    seriesDefaults: {
                        renderer:$.jqplot.DonutRenderer,// make this a donut chart.
                        rendererOptions:{
                            padding: 18,
                            innerDiameter : 30,
                            sliceMargin: 4, // Donut's can be cut into slices like pies.
                            ringMargin : 0,
                            startAngle: getStartAngle(),// Pies and donuts can start at any arbitrary angle.
                            shadowOffset : 2,
                            shadowDepth : 3,
                            highlightMouseOver : false,
                            dataLabels : 'label',
                            dataLabelFormatString : '%s',
                            dataLabelNudge : 50,
                            showDataLabels: true
                        }
                    },
                    seriesColors : ['#41556c', '#d13867']
                }
            },
            chartOptions = $.extend(true, defaults , chartInfo[type]);
        
        //app.log(chartOptions);
        $.jqplot.config.enablePlugins = true;

        function getStartAngle(){
            return 100 - options.data[0][1];
        }

        function getBarColor () {
            var colors = [], minColor = '#3a3735', maxColor = '#a8684c', maxIndex = 0, maxValue = options.data[maxIndex][1];

            options.data.forEach(function(v, i, a){
                colors.push(minColor);
                if(maxValue < v[1]){
                    maxValue = v[1];
                    maxIndex = i;
                }
            });
            colors[maxIndex] = maxColor;
            return colors;
        }

        return this.each(function(i, v){
            
            if(type == 'bar'){
                $.extend(chartOptions, {seriesColors: getBarColor()});
            }
            var $item = $(v);
            $item.jqplot([options.data], chartOptions);
        });
    };
    /*
	 * @name : jquery.count
	 * @desc : callback 함수로 count 반환.
	 */
    $.fn.count = function (options){
        
        var defaults = {
                'type' : 'byte', // 'char', 'byte'
                'readonly' : true,
                'max' : 80,
                'callback' : function () {},
                'useMember' : false
            },
            config = $.extend(true, defaults , options);
            isLogin = app.config('isLogin');

        function cutStringByByte($obj, max){
            var text = $obj.val(), leng = text.length;
            while(text.getByteLength() > max){
                leng--;
                text = text.substring(0, leng);
            }
            $obj.val(text);
        }

        return this.each(function(i, v){
            
            var $item = $(v), clength = 0,
                cMax = $item.attr('maxlength') || config.max;

            $item.on('keyup', handler).on('keydown', handler);

            if(config.readonly && config.useMember && !isLogin){
                $item.attr('readonly', true);
            } else {
                $item.attr('readonly', false);
            }

            function handler(e) {
                var keyCode = e.keyCode;
                
                //app.log(keyCode);

                if(keyCode != 8 && keyCode != 9 && keyCode != 16 && keyCode != 18 && keyCode != 27 && keyCode != 116){ // 8 : 'Backspace', 9 : 'Tab', 16 : 'Shift, 18 :'Alt', 27 : 'Esc', 116 : 'F5'
                    if(config.useMember && !isLogin){
                        app.goLogin();
                    } else {
                        $item.attr('readonly', false);
                        clength = config.type === 'char' ? $item.val().length : $item.val().getByteLength();

                        if (config.type === 'byte' && clength > cMax) {
                            alert('입력가능한 글자수를 초과했습니다.');
                            cutStringByByte($item, cMax);
                            clength = $item.val().getByteLength();
                            config.callback && config.callback (clength);
                            return false;
                        } else {
                        }
                        //app.log('clength : ' + clength);
                        config.callback && config.callback (clength);
                    }
                }
                
            } 
        });
    };
    /*
	 * @name : jquery.displayNumber
     * @depends : app.config
	 * @desc : 
	 */
    $.fn.displayNumber = function (){
        
        var defaults = {
                'type' : 'byte', // 'char', 'byte'
                'callback' : function () {}
            };
        
        return this.each(function(i, v){
            
            
            var $item = $(v), isLogin = app.config('isLogin');
            
            $item.on('focus', function () {
                if(!isLogin){
                    app.goLogin();
                    return false;
                }
            });
            $item.on('keydown', function () {
                if(!isLogin){
                    app.goLogin();
                    return false;
                }
            });
        });
    };
	/*
	 * @name : jquery.toggler
	 * @depends : language
	 * @desc : div tag 를 target 으로 method 실행.
	 * @desc : 노출/비노출을 base 로 추가 옵션 처리.
	 */
//	$.fn.toggler = function( options ){
//		var $target = this,
//			language = sochi.language,
//			defaults = {
//				val : '1',
//				data : [
//					{text : language.display.block, val : '1'}, 
//					{text : language.display.none, val : '0'}
//				]
//			},
//			config = $.extend(defaults , options),
//			cls = {btn : 'btn-toggle', listOpen : 'open'};
//		
//		function getBtn(val){
//			
//			var selectItemData = getItemData(val),
//			selectData = selectItemData ? selectItemData : config.data[0],
//			listHtml = '<div class="lists"><ul></ul></div>',
//			btnHtml = '<span><span>' + selectData.text + '</span><i class="ico-caret-down"></i></span>',
//			$btnSet = $('<div></div>').append(btnHtml).append(listHtml)
//			
//			config.data.forEach(function (v, i, a) {
//				$btnSet.find('ul').append('<li data-val="' + v.val + '">' + v.text + '</li>');
//			});
//			
//			return $btnSet;
//		};
//		
//		function setReturnData(data){
//			var obj = {};
//			
//			for(i in data){
//				obj[i] = data[i];
//			}
//			return obj;
//		};
//		function getItemData (_val) {
//			if(_val == '' && _val != 0) return null;
//			return config.data.filter(function(v){ return v.val == _val; })[0];
//		};
//		// set position
//		
//		// dom click
//		function documentClickHandler(e){
//			var clickTarget = e['target'] || e.srcElement;
//			if(clickTarget) {
//				var $clickTarget = $(clickTarget);
//				if($target.has($clickTarget).length == 0){ $target.removeClass('open'); }
//			}
//		};
//		documentClick.add(documentClickHandler);

//		return this.each(function (i, v) {
//			var $this = $(this), curVal = $this.data('val');
//			
//			curVal = curVal || curVal == 0 ? curVal : config.val;
//			
//			$this.data('val', curVal).addClass(cls.btn).html(getBtn(curVal).html());
//			$this.on('click', function(){
//				var $btn = $(this);

//				$target.filter(function (_i, _v) { return i != _i; }).removeClass('open');

//				if($btn.hasClass('open')){
//					$btn.removeClass('open');
//				} else {
//					$btn.addClass('open');
//				}
//				return false;
//			}).on('click', 'li', function () {
//				var utils = window.sochi.utils,
//					$item = $(this), thisVal = $item.data('val'), itemData = getItemData(thisVal);

//				if (curVal != itemData.val){
//					
//					$item.closest('.lists').parent().data('val', thisVal);
//					$item.closest('.lists').prev().find('span').text(itemData.text);
//					config.func && config.func(setReturnData($item.closest('.lists').parent().data()));
//					curVal = itemData.val;
//					utils.stateAlarm(itemData.text + '로 변경되었습니다.');
//				}
//			});
//		});
//	};
	/* 
	 * @name : checkboxGroup (jQuery Plugin : jQuery 1.7+)
	 * @version : 0.8
	 * @param : {Function} parent
	 * @param : {String} checkboxes selector
	 * @return : {jQuery Object} root checkbox
	 * @use :
	 * $(..).checkboxGroup({
	 * 		parent : function(){return this.closest('table');},
	 * 		selector : '...',
     * 		checkPermission : 1,
	 * });
	 */
	$.fn.checkboxGroup = function (options) {
		var _$this = this;
		if(_$this.length == 0) return;
		var $parent = options.parent.call(this),
			$elements = $parent.find(options.selector),
			checkPermission = options.checkPermission || $elements.length,
			tagName = _$this[0].tagName;
		
		//elements click
		$parent.off('click', options.selector).on('click', options.selector, elementsHandler);
		function elementsHandler (){
			var checkLength = $elements.filter('input:checked').length;
			towerCheck(checkPermission === checkLength);
			if(checkPermission === checkLength){
				$elements.filter('input:not(:checked)').prop('disabled', true);
			} else {
				$elements.filter('input:not(:checked)').prop('disabled', false);
			}
		};
		
		function towerCheck(checked){
            _$this.prop('checked', checked);
			if(tagName == 'BUTTON'){_$this.text(checked ? '전체해지' : '전체선택');}
		}
		if(checkPermission < $elements.length){
			_$this.remove();
		} else {
			_$this.attr('checked', false).off('click').on('click', function(){
				var checked = (_$this.prop('checked') ? true : false);
				towerCheck(checked);
				$elements.prop('checked', checked);
			});
		}
		return this;
	};
    $.fn.naturalSize = function () {
		var size = {width:0, height:0}, image;
		if(this[0]) {
            image = getImage(this[0]);
            size.width = image.width;
            size.height = image.height;
        }

        function getImage (DOMelement) {
		    var img = new Image();
		    img.src = DOMelement.src;
		    return {width: img.width, height: img.height};
	    };
		return size;
	};
	/* 
	 * @name : VideoPlayer (jQuery Plugin : jQuery 1.7+)
	 * @param : {Function} parent
	 * @param : {String} checkboxes selector
	 * @return : {jQuery Object} root checkbox
	 * @depends : 
	 * @use :
	 * $(..).videoPlayer({
	 * 		parent : function(){...},
	 * 		selector : '...'
	 * });
	 */
	$.fn.player = function (options) {
		var $target = this,
			iframeUrl = '',
			language = sochi.language,
			defaults = {
				id : 0,
				type : ''
			},
			config = $.extend(defaults , options);
		
		function getENVCode(type){
			var envCode = '';
			switch(type){
				case 'netv' :  envCode = 'winterolympic2014'; break;
				case 'vod' :  envCode = 'winterolympic2014_review'; break;
				default :  envCode = 'winterolympic2014'; break;
			}
			return envCode;
		}

		return this.each(function (i, v) {
			var $this = $(this);
			
			if(config.id && config.type){
				$this.prop({'src': iframeUrl + '?pmContentId=' + config.id + '&amp;pmENV=' + getENVCode(config.type)});
			}
		});
	};
    /* 
	 * @name : datePeriod
	 * @params : {jQuery Obect} start
	 * @params : {jQuery Obect} end
     * @params : {jQuery Obect} end
	 * @depends : 
	 * @use :
	 * $(..).datePeriod({
	 * 		start : ,
	 * 		end : 
	 * });
	 */
    $.fn.datePeriod = function(options){

        var $this = $(this),
        	nowDate = new Date(),
            defaults = {
                'data' : [
                    {'title': '2주일', 'data-period' : 2, 'data-type': 'w'}, 
                    {'title': '1개월', 'data-period' : 1, 'data-type': 'm'}, 
                    {'title': '3개월', 'data-period' : 3, 'data-type': 'm'}
                ]
            },
			config = $.extend(true, defaults , options);

        function getButton(data) {
            var $btn = $('<button></button>');
            $btn.attr(data)
            	.addClass('round gray')
            	.append($('<span />', { text: data.title }))
                .removeAttr('title')
            	.on('click', function() {
            		var $this = $(this);
            		setDate($this.data());
        			$this.offsetParent().find('button').removeAttr('title');
                    $this.offsetParent().find('button').removeClass('on');
                    $this.attr('title', '현재 선택됨');
        			$this.addClass('on');
                    
            		return false;
            	});

            return $btn;
        }



        function setDate(data) {
        	var startDate = new Date(), num = data['period'];

        	if(data['type'] === 'm') {
        		startDate.setMonth(nowDate.getMonth() - num);
        	} else {
        		startDate.setDate(nowDate.getDate() - (7*num));
        	}

            config.start.datepicker('setDate', startDate);
			config.end.datepicker('setDate', nowDate);
        }

        this.each(function (i, v) {
            config.data.forEach(function (v, i, a) {
                $this.append(getButton(v));
            });
        });
    };

    //특별관 자동 링크 처리
    $.fn.specialTheater = function (options) {

        return this.each( function (i, v) {
             var $this = $(this);
             var rcode = $this.data('regioncode');
             if (rcode) {
                if(rcode == "3D") {
                    $(this).css('cursor', 'default');
                } else {
                    $(this).css('cursor', '');
                }
            }

             $this.on("click", function () {
                var regionCode = $this.data('regioncode');

                if (regionCode) {
                    if(regionCode == "3D") {
                        return false;
                    }
                    
                    var url = "/theaters/special/?regioncode=" + regionCode;
                    if(regionCode == "MovieCollage") {
                        url = "/arthouse/";     //무비꼴라쥬일 경우 무비꼴라쥬 페이지로 이동
                    } 

                    top.location.href = url;
                } else {
                    if($this.length > 0) {
                        if($this[0].href) {
                            top.location.href = $this[0].href;
                        }
                    }
                }

                return false;
             });
        });

    };

    //////////////////////////////////////////
    //동영상 플레이어 (emkim)  (TODO:정리 필요)
    ////////////////////////////////////
    $.fn.moviePlayer = function(options){
    
        return this.each( function (i, v) {
			var $movie = $(v);
            $movie.on("click", function () {
                    var $this = $(this),
				    options = {
                        '$target': null,
                        'type' : 'player',
				        'html': $('#temp_popup_movie_player').html(),
				        'position': 'position',
				        'mask': true
				    };
                   
                    //layout setting
                    app.instWin.add(options);

                    //동영상+영화 정보 Setting
                    getTrailerInfo($this);

                    //신규동영상 Click event
                    $('.movie_player_inner_popup').on("click", function() {
                        getTrailerInfo($(this));
                        return false;
                    });

                    return false;
            });

            //동영상 + 영화정보 가져오기
            function getTrailerInfo($this) {

                var gIdx = $this.data('gallery-idx');
                if(!gIdx) { 
                    
                    
                    //gallery idx 존재하지 않을 경우 url존재하는지 check.

                    var url = $this.data('url');
                    if(url != "") {
                        //영상만 Setting

                        var ifrm = document.getElementById("ifrm_movie_player_popup");
                        ifrm.src= "/common/player/?autoplay=true&path=" + escape("http://h.vod.cgv.co.kr:80" + url);
                    }

                    return false; 
                }     

                 //상세정보 조회
                app.movie().getHDTrailerInfoWithMovieInfo({ "galleryIdx" : gIdx }, setTrailerInfo);
            }
            
            //동영상정보 setting
            function setTrailerInfo(result) {
                //app.log(result);
                if(!result) {return false;}
                
                //기존에 종료 layer 있으면 삭제
                $('#pop_player_relation_wrap').hide();

                //영화정보 : 여기에 이거 넣어도 되는걸까;
                if(result.MovieInfo) {
                    $("#movie_player_popup_movie_info").empty();
                    $("#temp_popup_movie_player_movie_info").tmpl(result.MovieInfo).appendTo("#movie_player_popup_movie_info");
                }

                //영상
                document.getElementById("ifrm_movie_player_popup").src= "/common/player/?autoplay=true&path=" + escape(result.FlashUrl) + "&poster=" + escape(result.ImageUrl);

                //제목
                var title = "";
                if(result.IsExclusive) { title += '<span class="ico-trailer monopoly">독점</span>'; }
                if(result.IsHD) { title += '<span class="ico-trailer hd">HD</span>'; }
                title += "[" + result.GroupTitle + "]" + result.Title
                $('#movie_player_popup_title').html(title);
                $('#movie_player_popup_caption').val(result.MovieCaption == "" ? "컨텐츠 준비 중 입니다." : result.MovieCaption);

                //성공 시 관련 영상 정보 가져오기
                app.movie().getHDTrailerRelationMovieTopList({ "movieIdx" : result.MovieIdx, "outGalleryIdx" : result.GalleryIdx, "limitCount" : 3 }, setRelationTrailer);

                //다시보기 버튼 활성화
                $('#pop_player_relation_wrap .btn-replay').attr('data-gallery-idx', result.GalleryIdx);
                
                //접근성으로 인해 X버튼 Focus out시 레이어팝업 닫힘
                $(".sect-layerplayer button.btn-close").focusout(
                    function() {
                      $(this).click();
                    }
                )
            }

            //해당 동영상과 관련있는 영상
            function setRelationTrailer(result) {
                if(!result) { return false; }

                $("#pop_player_relation_movie").empty();
                if(result.length > 0) {

                    $('#pop_player_relation_item_wrap').show();

                    $("#temp_popup_movie_player_relation_movie_item").tmpl(result).appendTo("#pop_player_relation_movie");

                    //신규동영상 Click event
                    $('.movie_player_inner_popup').on("click", function() {
                        getTrailerInfo($(this));
                        return false;
                    });
                }
                else {

                    $('#pop_player_relation_item_wrap').hide();
                }
            }
        });
    };

})( jQuery, window, document );