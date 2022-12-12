;
// ** objest list **
// app.utils

/*
* @name : app.utils
* @desc : util package
* -
*/
app.utils = {
    /*
    * @name : movie
    * @desc : movie ajax
    * @depends: jquery.js
    */
    movie: function () {
        var app = window.app;

        return {
            getList: function (data, callback) {
                var url = '/common/ajax/movies.aspx/GetMovieMoreList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getTopList: function (data, callback) {
                var url = '/common/ajax/movies.aspx/GetMovieTopList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getHDTrailerSearchList: function (data, callback) {
                var url = '/common/ajax/movies.aspx/GetHDTrailerSearchList';
                //app.log(data);
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getHDTrailerInfoWithMovieInfo: function (data, callback) {
                var url = '/common/ajax/movies.aspx/GetHDTrailerInfoWithMovieInfo';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getHDTrailerRelationMovieTopList: function (data, callback) {
                var url = '/common/ajax/movies.aspx/GetHDTrailerRelationMovieTopList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setPointReview: function (data, callback) {
                var url = '/common/ajax/point.aspx/AddData';
                //app.log(data);
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getPointSearchList: function (data, callback) {
                var url = '/common/ajax/point.aspx/GetMoviePointList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getViewUser: function (data, callback) {
                var url = '/common/ajax/point.aspx/GetIsMovieViewUser';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            removePoint: function (data, callback) {
                var url = '/common/ajax/point.aspx/RemovePointData';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            removePointCheck: function (data, callback) {
                var url = '/common/ajax/point.aspx/RemovePointDataCheck';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getReviewSearchList: function (data, callback) {
                var url = '/common/ajax/point.aspx/GetMovieReviewList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getReviewDetail: function (data, callback) {
                var url = '/common/ajax/point.aspx/GetMovieReview';
                //app.log(data);
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            removeReview: function (data, callback) {
                var url = '/common/ajax/point.aspx/RemoveReviewData';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            addMovieReviewCommunityAdmit: function (data, callback) {
                var url = '/common/ajax/point.aspx/AddMovieReviewCommunityAdmit';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getCuratorVoiceInfo: function (data, callback) {
                var url = '/common/ajax/collage.aspx/GetCuratorVoiceInfo';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getCuratorVoiceList: function (data, callback) {
                var url = '/common/ajax/collage.aspx/GetCuratorVoiceList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getCuratorVoiceList2: function (data, callback) {
                var url = '/common/ajax/collage.aspx/GetCuratorVoiceList2';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getMovieDiaryList: function (data, callback) {
                var url = '/common/ajax/movielog.aspx/GetMovieDiaryList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getMovieTrailerList: function (data, callback) {
                var url = '/common/ajax/movielog.aspx/GetTrailerList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getMovieStillCutList: function (data, callback) {
                var url = '/common/ajax/movielog.aspx/GetStillCutList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setUpload: function (form, callback) {
                var url = "/common/upload/fileupload.aspx";
                app.ajax().form({ url: url, form: form, successHandler: callback });
            },
            getPointSearchVariableList: function (data, callback) {		//2014.12 평점UI개선 : 좋아요 증가
                var url = '/common/ajax/point.aspx/GetMoviePointVariableList';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setCommentGoodInsert: function (data, callback) {	//2014.12 평점UI개선 : 좋아요 증가
                var url = '/common/ajax/point.aspx/setCommentGoodInsert';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setCommentGoodDelete: function (data, callback) {	//2014.12 평점UI개선 : 좋아요 감소
                var url = '/common/ajax/point.aspx/setCommentGoodDelete';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setCommentSpoilerInsert: function (data, callback) {	//2014.12 평점UI개선 : 스포일러 신고
                var url = '/common/ajax/point.aspx/setCommentSpoilerInsert';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setCommentSpoilerDelete: function (data, callback) {	//2014.12 평점UI개선 : 스포일러 해지
                var url = '/common/ajax/point.aspx/setCommentSpoilerDelete';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setCommentReportInsert: function (data, callback) {	//2014.12 평점UI개선 : 욕설/비방 신고
                var url = '/common/ajax/point.aspx/setCommentReportInsert';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setCommentReportDelete: function (data, callback) {	//2014.12 평점UI개선 : 욕설/비방 해지
                var url = '/common/ajax/point.aspx/setCommentReportDelete';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getCommentMy: function (data, callback) {	//2014.12 평점UI개선 : 내가쓴 평점 내용 불러오기
                var url = '/common/ajax/point.aspx/getCommentMy';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            setCommentEdit: function (data, callback) {	//2014.12 평점UI개선 : 평점수정하기
                var url = '/common/ajax/point.aspx/setCommentEdit';
                app.ajax().set({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            },
            getCommentTabCnt: function (data, callback) {	//2014.12 평점UI개선 : 내가쓴 평점 내용 불러오기
                var url = '/common/ajax/point.aspx/getCommentTabCnt';
                app.ajax().get({ dataType: 'json', url: url, data: data, contentType: "application/json; charset=utf-8", successHandler: callback });
            }
        }
    },
    /*
    * @name : ajax
    * @desc : ajaxWrapper
    * @params : options
    * @depends: jquery.js
    */
    ajax: function () {
        var app = window.app;

        function getUrl(url) {
            url = hasProtocol(url) ? url : app.config('webDomain') + url;

            function hasProtocol(url) {
                var protocols = ['http', 'file'], has = false;
                protocols.forEach(function (v, i, a) {
                    if (!has) { if (url.indexOf(v) > -1) has = true; }
                });
                return has;
            }
            return url;
        }
        return {
            form: function (options) {

                var url = getUrl(options.url), _loading = app.loading();

                if (!options.url) return app.errorHelper('not defined url!');
                if (!options.form || options.form.length === 0) return app.errorHelper('not defined form(jQuery)!');

                $(options.form).attr('action', url);

                if (typeof $.fn.ajaxSubmit == 'function') {
                    $(options.form).ajaxSubmit({
                        url: options.url,
                        beforeSubmit: _loading.show,
                        success: function (result) {
                            //app.log('======================');
                            _loading.hide();
                            //app.log(result);
                            result = $.parseJSON(result);
                            if (!result.hasErrors) {
                                options.successHandler && options.successHandler(result);
                            } else {
                                app.errorHandler(result);
                            }
                        }
                    });
                }
            },
            get: function (options) {
                if (!options.url) $.error('not defined url.');
                var url = getUrl(options.url),
                    defaults = {
                        type: "GET",
                        url: url,
                        data: options.data
                    },
                    config = $.extend(defaults, options);

                config.url = url;

                //app.log('[ajax] get url : ' + url);
                //app.log(options.data);

                $.ajax(config).done(function (result) {
                    //app.log('[ajax] get result : ', result);
                    //app.log(result);
                    var r = result;
                    if (config.dataType === 'json' && r.d) {
                        r = $.parseJSON(result.d);
                    }

                    options.loading && options.loading.hide();
                    if (!result.hasErrors) {
                        options.successHandler && options.successHandler(r);
                    } else {
                        app.errorHandler(r);
                    }
                }).fail(function (jqxhr, textStatus, error) {
                    options.loading && options.loading.hide();
                    app.failHandler(error);
                });
            },
            getp: function (options) {
                var url = getUrl(options.url);

                //app.log('[ajax] get url : ' + url);
                //app.log(options.data);

                $.ajax({ url: url, data: options.data, dataType: 'jsonp' })
					.done(function (result) {

					    //app.log('[ajax] get result : ', result);
					    //app.log(result);
					    options.loading && options.loading.hide();
					    if (!result.hasErrors) {
					        options.successHandler && options.successHandler(result);
					    } else {
					        app.errorHandler(result);
					    }
					}).fail(function (jqxhr, textStatus, error) {
					    options.loading && options.loading.hide();
					    app.failHandler(error);
					});
            },
            set: function (options) {
                var app = window.app,
					url = getUrl(options.url),
                    defaults = {
                        type: "POST",
                        url: url,
                        data: options.data
                    },
                    config = $.extend(defaults, options);

                config.url = url;

                //app.log('[ajax] set url : ' + url);
                //app.log(options.data);
                //app.log(config);

                $.ajax(config)
					.done(function (result) {
					    options.loading && options.loading.hide();
					    //app.log('[ajax] set result : ', result);
					    //app.log(result);

					    var r = result;
					    if (config.dataType === 'json' && r.d) {
					        r = $.parseJSON(result.d);
					    }

					    if (!result.hasErrors) {
					        options.successHandler && options.successHandler(r);
					    } else {
					        app.errorHandler(r);
					    }
					}).fail(function (jqxhr, textStatus, error) {
					    options.loading && options.loading.hide();
					    app.failHandler(error);
					});
            }
        }
    },
    /*
    * @name : instWin [Function]
    * @params : object
    * @depends: jquery.js
    * @desc : instance Window
    * @desc : default position fixed.
    */
    // TODO : 레이어 올리기.
    // TODO : Focus Roof.
    // TODO : type='photo' 인 경우, 가운데로 위치 이동.

    instWin: new function () {
        var app = window.app, mask = null,
			defaults = {
			    'type': 'contents',    // 'contents', 'photo', 'player', 'href'
			    'position': 'absolute',
			    'mask': 'none',
			    'data': [],
			    'offset': 0,    // photo 에서 시작점.
			    'title': '[팝업제목]',
				'independence': false
			}, arrWin = [], that = {};

        var InstWin = function (config) {
            var that = this;
            this.index = config.offset;
            this.type = config.type;
			this.independence = config.independence;

            if (this.type == 'player') {
                //player일 경우 target무조건 null처리 (레이어 팝업 한페이지에서 여러개 띄울 경우 기존 값 남아있음)
                config.$target = null
            }

            var getContents = {
                'photo': function () {
                    var $slide = $('<div class="slider">'
                            + '<button type="button" class="btn-prev">이전 페이지 이동</button>'
                            + '<button type="button" class="btn-next">다음 페이지 이동</button>'
                            + '</div>');

                    $slide.prepend(getItems());

                    function getItems() {
                        var item = '';
                        $.each(config.data, function (i, v) {
                            item += '<div class="item-wrap">'
                        	+ '<div class="item">'
                            + '<img src="' + v['imageUrl'] + '" alt="' + v['alt'] + '" />'
                            + '</div>'
                            + '</div>'
                        });
                        return item;
                    }
                    return $('<div class="layer-contents"></div>').append($slide);
                },
                'contents': function () {
                    return $(config.html);
                },
                'center': function () {
                    return $(config.html);
                },
                'player': function () {
                    return $(config.html);
                },
                'href': function () {
                    var href = config.href;

                    var $temp = $('<div></div>');
                    $temp.load(config.href, function (response, status, xhr) {
                        //app.log('11');
                    });

                    //app.log($temp);
                    //app.log($temp.html());
                    return $temp;
                }
            };

            function init() {
                // index 설정은 창을 닫을때 현재 인덱스를 가져와야 하면 조정이 필요함,. 아니라면 그냥 config.offset.
                var $body = $(document.body), index = config.offset,
                    $layer = $('<div class="layer-wrap" style=""></div>'),
                    $btn = $('<button class="btn-close">' + config.title + ' 닫기</button>'),
                    $contents = getContents[config.type]();

                $layer.data('type', config.type);
                // 팝업 정의 후, 재작업.
                if (config.$target) {
					if(!(config.type === 'center')) {
                    config.$target.after($layer.append($contents));
                } else {
                    $body.append($layer.append($contents));
                }
                } else {
                    $body.append($layer.append($contents));
                }

                if (config.type === 'photo') {

					if($(document).find('#stillcut_list').length > 0 || $(document).find('#theater_img_container').length > 0) {
						$layer.addClass('stillcut-viewer');
					}

                    $contents.append($btn);
                    $layer.css({ 'margin-top': -parseInt($contents.height() / 2, 10), 'margin-left': -parseInt($contents.width() / 2, 10), 'position': 'fixed' });   // set position photo viewer
                    $contents.find('.slider').visualMotion({ 'type': config.type, 'callback': callbackHandler, 'offset': config.offset });

                    //set focus
                    $layer.find('a, button').on('keyup', focusHandler).on('keydown', focusHandler).first().focus();


                } else if (config.type === 'player' || config.type === 'center') {

					var windowH = $(window).height(),
						contW = $contents.width(),
						contH = $contents.height();

                    //동영상 팝업 윈도우사이즈보다 작은 경우 짤리는 현상 해결을 위해
                    var position = "", top = 0;

                    if (windowH >= contH) {
                        position = "fixed";
                        top = -parseInt(contH / 2, 10);
                    } else {
                        position = "absolute";
						top = $(window).scrollTop() - ((contH / 2) - 200);
                    }

                    $layer.css({ 'margin-top': top, 'margin-left': -parseInt(contW / 2, 10), 'position': position });   // set position player viewer

					//set focus
                    $layer.attr('tabindex','0').focus();
                }

                var moveFirst = false;
                function focusHandler(e) {
                    var keyCode = e.keyCode;
                    if (keyCode == 9) {
                        if (moveFirst) {
                            $layer.find('a, button').first().focus();
                            moveFirst = false;
                            return false;
                        }
                        if ($(this)[0] == $layer.find('a, button').last()[0]) {
                            moveFirst = true;
                            return false;
                        }
                    }

                }

                $contents.find('button.btn-close').on('click', function (e) {

                    //close 시 IE에서 플레쉬 있는 상태에서 페이지를 떠날경우 하기 에러 발생
                    //__flash__removeCallback 해당 문제 해결을 위해 해당 iframe src 자체 변경
                    if (config.type === 'player') {
                        setTimeout(function () {
                            $contents.find('iframe').attr('src', '');
                            setTimeout(function () {
                                remove();
                            }, 80);
                        }, 120);
                    } else {
						if(config.independence) {
							$contents.parents('.layer-wrap').remove();
							mask.hide();
						}else{
	                        app.log('## close');
	                        remove();
						}
                    }

					if(config.$target){
					config.$target.attr('tabindex','0').focus();
					}

                    if (config.type === 'photo') {
                        location.hash = 'tile_' + index;
                    }

                    //layer close할 때 type default값으로 적용 (plyaer 팝업 열어다 닫으면 player 팝업으로 유지 됨)
                    config.type = 'contents';

                    return false;
                });

                function callbackHandler(_index) {
                    index = _index;
                    if (config.type === 'photo' && !$('tile_' + _index).length) {
                        config.more && config.more();
                    }
                }
            }

            init();
        };



        function add(options) {
            //app.log('##instWin add');


            mask = app.mask();

            var config = $.extend(defaults, options);

            arrWin.forEach(function (v, i, a) {
                if (v.type === 'contents') {
                    remove(v.index);
                    a.splice(v.index, 1); // 배열 원소 제거 로직 필요.
                }
            });

            if (config.mask != 'none') {    // options.type 이 없는 경우, type : default 'contents', contents 인 경우, 기본 mask 없음.
                mask.show();
            }
            config.index = arrWin.length;
            arrWin.push(new InstWin(config));
        };

        // destroy viewer
        function remove(_index) {
            var targetIndex = _index || arrWin.length;

            var $body = $(document.body);
            $body.find('.layer-wrap').remove();
            mask.hide && mask.hide();
        };

        that.add = function (options) {
            add(options);
        };
        that.remove = remove;

        return that;
    },
    /*
    * @name : htmlLoad [Function]
    * @desc :
    * @params : object
    * @depends: config [Object]
    */
    htmlLoad: function ($target, href) {

        var $tempLayer = $('<div></div>');
        if (!$tempLayer.html()) {
            $tempLayer.load(href, function (response, status, xhr) {
                openWin(response);
            });
        }

        function openWin(html) {
            var options = {
                '$target': $target,
                'html': html
            };
            app.instWin.add(options);
        }
        return $tempLayer;
    },
    htmlLoad2: function (options, href) {

        var $tempLayer = $('<div></div>');
        if (!$tempLayer.html()) {
            $tempLayer.load(href, function (response, status, xhr) {
                openWin(response);
            });
        }

        function openWin(html) {

            if (options == null) return;



            options.html = html;
            app.log(html);

            app.instWin.add(options);
        }
        return $tempLayer;
    },
    /*
    * @name : log [Function]
    * @desc : console log.
    * @params : object
    * @depends: config [Object]
    */
    log: function (obj) {
        var useLog = app.config('useLog') == true && window.console;
        if (useLog) {
            if (typeof obj == "object" && console.dir) {
                console.dir && console.dir(obj);
            } else {
                console.log && console.log(obj);
            }
        }
    },
    /*
    * @name : errorHandler [Function]
    * @desc : error 처리.
    * @params : object
    */
    errorHandler: function (error) {
        var app = window.app;

        error = error.data ? error.data : error;
        app.errorHelper(error);
        //		app.stateAlarm(error);
    },
    /*
    * @name : errorHelper [Function]
    * @desc : throw
    * @params : object
    */
    errorHelper: function (text) {
        //window.app.log(text);
        throw new Error(text);
    },
    /*
    * @name : failHandler [Function]
    * @desc : fail 처리.
    * @params : object
    */
    failHandler: function (fail) {
        var app = window.app;

        fail = fail.data ? fail.data : fail;
        app.errorHelper(fail);
        //		app.stateAlarm(fail);
    },
    /*
    * @name : mask [Object]
    * @desc : mask layer
    * @depends: jquery.js
    */
    mask: function () {
        var cls = 'mask',
			$template = $('<div class="' + cls + '" style=""></div>'),
			css = {
			    'position': 'fixed',
			    'left': '0',
			    'top': '0',
			    'width': '100%',
			    'height': '100%',
			    'z-index': '100',
			    'background-color': 'rgb(0,0,0)',
			    'filter': 'alpha(opacity=80)',
			    'background-color': 'rgba(0, 0, 0, 0.8)'
			    //'background': 'url("' + app.config('staticDomain') + 'images/common/bg/bg_pop_dim80.png") 0 0 repeat'
			},
            $body = $(document.body),
            $target;

        return {
            show: function (options) {
                if (options && options.target) {
                    $target = options && options.target;
                    css.position = 'absolute';
                    css.filter = 'alpha(opacity=50)';
                    css['background-color'] = 'rgba(0, 0, 0, 0.5)';
                } else {
                    $target = $body;
                }

                //app.log('## mask show');
                //app.log($body.find('.' + cls).length);

                if ($body.find('.' + cls).length === 0) {
                    $template.css(css);
                    $target = (options && options.target) || $body;

                    //app.log($target);
                    //app.log($template);
                    //app.log('##end');

                    $target.append($template);
                    isMask = true;
                }
            },
            hide: function () {
                if (!$body.find('>.layer-wrap').length) {
                    app.log('mask hide');

                    $body.find('.' + cls).remove();
                    isMask = false;
                }
            }
        };
    },
    /*
    * @name : loading [Object]
    * @desc : loading layer
    * @depends: jquery.js
    */
    loading: function () {
        var isLoading = false,
			cls = 'loading',
			$template = $('<div class="' + cls + '"></div>'),
            circleType = { 'default': 'images/common/ico/ico_loading.gif', 'large': 'images/common/ico/ico_loading_large.gif' },
            css = {
                'position': 'fixed',
                'left': '50%',
                'top': '50%',
                'width': '32px',
                'height': '32px',
                'margin': '-16px 0 0 -16px',
                'z-index': '1000',
                'background': 'url("' + app.config('staticDomain') + circleType['default'] + '")'
            }, mask = app.mask(), $body = $(document.body), $target;


        return {
            show: function (options) {
                var useMask = true;
                if (!isLoading) {
                    if (options && options.target) {
                        $target = options && options.target;
                        css.position = 'absolute';
                        //app.log($target);
                    } else {
                        $target = $body;
                    }

                    if (options && !options.mask) useMask = false;
                    if (useMask) mask.show(options);

                    if (options.circleType === 'large') {
                        $template.css({
                            'position': 'absolute',
                            'left': '50%',
                            'top': '50%',
                            'width': '100px',
                            'height': '100px',
                            'margin': '-50px 0 0 -50px',
                            'background': 'url("' + app.config('staticDomain') + circleType['large'] + '")'
                        });
                    } else {
                        $template.css(css);
                    }

                    $target.append($template).show();
                    isLoading = true;
                    setTimeout(app.loading().hide, 5000);
                }
            },
            hide: function () {
                mask.hide();
                $(document.body).find('> .' + cls).remove();
                isLoading = false;
            }
        };
    },
    /*
    * @name : imageLoad [Function]
    * @desc : image onload event
    */
    imageLoadResize: function (_this, maxSize) {
        var $this = $(_this),
			n_width = $this.prop('naturalWidth'),
			n_height = $this.prop('naturalHeight');

        maxSize = maxSize ? maxSize : 192;
        //108*192
        //192*108

        if (n_width < n_height) {
            if (n_height > maxSize) {
                $this.css('height', maxSize);
            }
        } else {
            if (n_width > maxSize) {
                $this.css('width', maxSize);
            }
        }
    },
    /*
    * @name : htmlMapper [Function]
    * @desc :
    */
    htmlMapper: function (options) {
        var $this = $(_this),
			n_width = $this.prop('naturalWidth'),
			n_height = $this.prop('naturalHeight');

        if (n_width < n_height) {
            if (n_height > maxSize) {
                $this.css('height', maxSize);
            }
        } else {
            if (n_width > maxSize) {
                $this.css('width', maxSize);
            }
        }
    },
    /*
    * @name : isArray [Function]
    * @desc :
    */
    isArray: function (obj) {
        return Object.prototype.toString.call(obj) === '[object Array]';
    },
    /*
    * @name : goLogin [Function]
    * @desc :
    */
    goLogin: function () {
        //        if (app.config('isLogin')) {
        //            return true;
        //        } else {
        if (confirm(_LANGUAGE.loginConfirm)) {
            top.location.href = "/user/login/?returnURL=" + escape(top.location.href);
        }
        return false;
        //        }
    },
    /*
    * @name : movieInfo
    * @desc :
    */
    movieInfo: function (_this, options) {
        var $this = $(_this);

        return {
            reset: function () {
                $('.point').point();
                $(".btn-like").like();
            }
        }
    },
    /*
    * @name : addNumber [Function]
    * @params : v
    * @params : i
    * @desc :
    */
    addNumber: function (v, i) {
        if (typeof v != 'string' || typeof i != 'number') return;
        v = v.trim().replace(',', '');
        try {
            v = parseInt(v, 10);
            v = v + i;
        } catch (e) { }

        v = v.formatMoney();
        //app.log(v);
        return v;
    }
    /*
    * @name : RGBToHex [Function]
    * @desc : convert RGB to Hex.
    */
    //    RGBToHex: function (rgb) {
    //        var hex = [
    //			rgb.r.toString(16),
    //			rgb.g.toString(16),
    //			rgb.b.toString(16)
    //		];
    //        $.each(hex, function (nr, val) {
    //            if (val.length == 1) {
    //                hex[nr] = '0' + val;
    //            }
    //        });
    //        return hex.join('');
    //    },
    /*
    * @name : HexToRGB [Function]
    * @desc : convert Hex to RGB.
    */
    //    HexToRGB: function (hex) {
    //        var hex = parseInt(((hex.indexOf('#') > -1) ? hex.substring(1) : hex), 16);
    //        return { r: hex >> 16, g: (hex & 0x00FF00) >> 8, b: (hex & 0x0000FF) };
    //    },
    /*
    * @name : RGBFromBG [Function]
    * @desc : get rgb from background.
    */
    //    RGBFromBG: function (rgba) {
    //        var rgbMatch = /\d+, \d+, \d+/,
    //			matchRGB = rgba.match(rgbMatch).length && rgba.match(rgbMatch)[0].split(',');
    //        return { r: parseInt(matchRGB[0].trim(), 10), g: parseInt(matchRGB[1].trim(), 10), b: parseInt(matchRGB[2].trim(), 10) };
    //    }
}
;

/*
* @name : share
* @depends: jquery.js
* @desc : SNS Button Event Handler
* @interface : twitter, facebook
*/
var share = new function () {
    var app = window.app, that = {},
        title = $('#ctl00_og_title').attr('content'),
        pageUrl = location.href,
        twitterShare = 'http://twitter.com/home/?status=',
        facebookShare = 'http://www.facebook.com/sharer.php?s=100';

    function getParamString(params) {
        var strParams = '?';
        $.each(params, function (i, v) {
            if (v != '') strParams += i + '=' + v + '&';
        });
        return strParams;
    }

    that.twitterHandler = function (e) {

        // long url.
        addParams = encodeURIComponent("[CGV]" + title + "\n" + pageUrl);
        window.open(twitterShare + addParams, 'share_twitter', 'width=640, height=440');

        return false;

        //or short url.
        app.ajax().get({
            none_loading: true,
            url: app.config('bitlyUrl'),
            data: { long_url: params.original_referer },
            successHandler: function (result) {

                var url = result.data.url;
                params.original_referer = url;
                params.counturl = url;

                addParams = getParamString(params);
                window.open(encodeURI(twitterShare + addParams), 'share_twitter', 'width=640, height=440');
            }
        });

        return false;
    };
    that.facebookHandler = function (e) {

        var addParams = '&p[title]=' + encodeURIComponent(title)
                        + '&p[summary]=' + encodeURIComponent($('#ctl00_og_description').attr('content'))
                        + '&p[url]=' + encodeURIComponent(pageUrl);

        window.open(facebookShare + addParams, 'share_facebook', 'directories=no,location=no,menubar=no,status=no,toolbar=no,scrollbars=no,resizable=no,width=420,height=370');

        return false;
    };

    return that;
};

var loadImage = function (_this, options) {
    //app.log('loadImage');
}
/*
* @name : errorImage
* @desc : images onerror event.
* small, portrait, square / default : square
* <img src="" onerror="errorImage(this, {'type', 'small'});" />
*/
var errorImage = function (_this, options) {
	var $this = $(_this), imgUrl = '';
	options = options || {'type':'square'}; // set square to default
	if (!window._NO_IMAGE) {
		throw new Error('not defined _NO_IMAGE enum.');
		return;
	}
	imgUrl = window._NO_IMAGE[options.type];

	if ($this.data('error-src')) return;

	$this.data({ 'origin-src': $this.attr('src'), 'error-src': imgUrl });
	options.src = imgUrl;
	$this.prop(options);
};

//paging setting
var setPagingNavigation = function (totalCount, pageSize, pagingId, containerId, callback) {

    if (totalCount < 1) {
        $(pagingId).empty();
        $(containerId).html("<li style='width:100%;text-align:center;padding:30px 0;'>해당 조건에 데이터가 존재하지 않습니다.</li>");
        return;
    }

    var pageCount = parseInt(Math.ceil(totalCount / pageSize));   //pageCount
    $(pagingId).paging(
        {
            max: pageCount,
            item: 'li',
            itemCurrent: 'on',
            itemClass: '',
            format: '<a href="#{0}" title="{7}">{0}</a>',
            first: '<button class="btn-paging first" type="button">처음</button>',
            prev: '<button class="btn-paging prev" type="button">이전 10개</button>',
            next: '<button class="btn-paging next" type="button">다음 10개</button>',
            last: '<button class="btn-paging end" type="button">끝</button>',
            onclick: function (e, page) {
                if (typeof callback === "function") {
                    callback(page);
                }
            }
        }
    );
};
//paging setting - totalCount 0 일때 html리턴값없음
var setPagingNavigation2 = function (totalCount, pageSize, pagingId, containerId, callback) {

    if (totalCount < 1) {
        $(pagingId).empty();
        //$(containerId).html("<li style='width:100%;text-align:center;padding:30px 0;'>해당 조건에 데이터가 존재하지 않습니다.</li>");
        return;
    }

    var pageCount = parseInt(Math.ceil(totalCount / pageSize));   //pageCount
    $(pagingId).paging(
        {
            max: pageCount,
            item: 'li',
            itemCurrent: 'on',
            itemClass: '',
            format: '<a href="#{0}" title="{7}">{0}</a>',
            first: '<button class="btn-paging first" type="button">처음</button>',
            prev: '<button class="btn-paging prev" type="button">이전 10개</button>',
            next: '<button class="btn-paging next" type="button">다음 10개</button>',
            last: '<button class="btn-paging end" type="button">끝</button>',
            onclick: function (e, page) {
                if (typeof callback === "function") {
                    callback(page);
                }
            }
        }
    );
};


//자주가는 CGV 팝업창에서 재셋팅해 줘야 하는 곳이 있어서 별도 분리해야 함.
var setFavMovieLink = function () {
    $('#favoriteTheaters a').on('click', function () {
        if (app.config('isLogin')) {
            if ($(this).data('theatercode').length > 0) {

                var theatercode = $(this).data('theatercode');
                var regioncode = $(this).data('regioncode');
                var date = $(this).data('selecteddate')

                if (regioncode == "103") {
                    location.href = "/theaters/special/show-times.aspx?regioncode=103&theatercode=" + (theatercode == "P004" ? "0089" : "0040");        //씨네드쉐프

                } else if (regioncode == "CK" && theatercode == "K049") {
					//CINE KIDS 북수원
					location.href = "/theaters/special/show-times.aspx?regioncode=CK&theatercode=0049";  //CINE KIDS 북수원
                } else {
                    location.href = "/theaters/?theatercode=" + theatercode
                                + (regioncode ? "&areacode=" + regioncode : "")
                                + (date ? "&date=" + date : "");
                }
            }
            else {
                //ToDO : 윈도우 팝업창 공통화 하기
                var win = window.open("/user/popup/favoritetheaters.aspx", "url", "left=0,top=0,width=645,height=370,toolbar=no,scrollbars=no");
                win.focus();
            }
        }
        else {
            app.goLogin();
        }

        return false;
    });
};

//평점쓰기,보기 팝업

var openPointPopUp = function (buttonObj) {
    var commentIdx = buttonObj.attr('data-cidx');
    var watchingIdx = buttonObj.attr('data-widx');
    var movieIdx = buttonObj.attr('data-midx');
    var url, win;

    if (commentIdx == '0' || commentIdx == '') {
        url = "/user/popup/write-point.aspx?cidx=" + commentIdx + "&widx=" + watchingIdx + "&midx=" + movieIdx;
        win = window.open(url, "winPointWrite", "left=0,top=o,width=800,height=420,toolbar=no,scrollbars=no");
    }
    else {
        url = "/user/popup/view-point.aspx?cidx=" + commentIdx + "&widx=" + watchingIdx + "&midx=" + movieIdx;
        win = window.open(url, "winPointView", "left=0,top=o,width=800,height=300,toolbar=no,scrollbars=no");
    }
    win.focus();
};

//movie diary
var moviediary = new function () {

    //var currentIdx = 0;
    var watchedList = [];
    var that = {};
    var choiceMoveInfo = { watchedIdx: 0, movieIdx: 0 };
    var choiceData = [];

    that.init = function (data) {

        if (data) {
            if (watchedList.length < 1) {
                watchedList = data;
            }
        }

        var isUserChoice = false;
        var $imageTyp1 = $('#hdnImageType1').val();
        var $imageTyp2 = $('#hdnImageType2').val();
        var $imageTyp3 = $('#hdnImageType3').val();
        var $imageTyp4 = $('#hdnImageType4').val();


        choiceMoveInfo.movieIdx = $('#movieidx').val()

        //스틸컷
        if ($imageTyp1 != "-1") {
            isUserChoice = true;
            choiceData.push({ 'typeCode': '101', 'imageURL': (app.config('imageDomain') + $('#hdnImagePath1').val()) });      //DB에 등록된 데이터는 도메인 없음. 도메인 붙여줘야 함.
            $('#btn_stillcut').parent('li').addClass("on");  //button on 처리
        }

        //동영상
        if ($imageTyp2 != "-1") {
            isUserChoice = true;
            choiceData.push({ 'typeCode': '201', 'imageURL': (app.config('imageDomain') + $('#hdnImagePath2').val()) });      //DB에 등록된 데이터는 도메인 없음. 도메인 붙여줘야 함.
            $('#btn_trailer').parent('li').addClass('on');  //button on 처리
        }

        //사용자 업로드
        if ($imageTyp4 != "-1") {
            isUserChoice = true;
            choiceData.push({ 'typeCode': '301', 'imageURL': (app.config('imageDomain') + $('#hdnImagePath4').val()) });      //DB에 등록된 데이터는 도메인 없음. 도메인 붙여줘야 함.
            $('#btn_upload').parent('li').addClass("on");  //button on 처리
        }

        if (isUserChoice) //사용자가 선택한 아이템이 있는 경우 display
            that.setUserChoice();
    }

    that.movieListHandler = function ($this) {

        if (watchedList == null || watchedList.length < 1) {
            alert("무비다이어리를 작성할 영화가 존재하지 않습니다.");
            return false;
        }

        //layout setting
        var $std = $this,
                    options = {
                        '$target': $std,
                        'html': $('#temp_watched_wrap').html(),
                        'position': 'position',
                        'mask': 'none'

                    };
        app.instWin.add(options);

        //item setting
        if ($('#watched_item_list')) {
            $('#temp_watched_item').tmpl(watchedList).appendTo($('#watched_item_list'));
        }

        //Layout 디자인스크롤 적용
        $('#layout_watched').css({ width: 692, height: 333 }).customScrollbar();

        $('#watched_item_list button').on('click', function () {
            that.setWatchedIdx($(this).val());
        });

        return false;
    }

    that.setWatchedIdx = function (idx) {

        var selectItem = null;

        if (idx < 0) return;
        for (var i = 0; i < watchedList.length; i++) {
            if (watchedList[i].WatchingIdx == idx) {
                selectItem = watchedList[i];

                //poster setting
                $('#temp_watched_select_item').tmpl(selectItem).replaceAll($('.article-any-movie > a'));
                $('.my-point').point();
                break;
            }
        }

        //app.log(selectItem);
        if (idx > 0) {
            choiceMoveInfo.watchedIdx = idx;        //watched idx
            choiceMoveInfo.movieIdx = selectItem.MovieIdx //movie idx

            $('#watchedIdx').val(idx);
            $('.layer-wrap').remove();
        }
    }

    that.removeWatchedIdx = function () {
        if (choiceMoveInfo.watchedIdx > 0) {
            $('#watchedIdx').val('0');
            choiceMoveInfo.watchedIdx = 0;
            choiceMoveInfo.movieIdx = 0;
            $('.diary-register-wrap div.article-any-movie').html('<a href="#" title="영화리스트 열림"><span><em>어떤 영화를 보셨나요?</em></span><i>열림</i></a>');
        }
    }

    that.setChoiceData = function (type_code, img_url, url) { //사용자가 선택한 3종셋트 data setting

        switch (type_code) {

            case ('201'):       //trailer

                if (url == "") {

                    //thumb_url
                    $('#hdnImageType2').val('-1');
                    $('#hdnImagePath2').val('');

                    //trailer_url
                    $('#hdnImageType3').val('-1');
                    $('#hdnImagePath3').val('');
                    $('#hdnImageGalleryIdx3').val('');    //GalleryIdx값 Null처리

                    $('#btn_trailer').parent('li').removeClass('on');  //button off 처리

                } else {

                    //thumb_url
                    $('#hdnImageType2').val('201');
                    $('#hdnImagePath2').val(that.getPath(img_url));

                    //trailer_url
                    $('#hdnImageType3').val('202');
                    $('#hdnImagePath3').val(that.getPath(url));

                    $('#btn_trailer').parent('li').addClass('on');  //button on 처리

                }

                break;

            case ('101'):  //still cut
                $('#hdnImageType1').val((img_url == "" ? '-1' : '101'));
                $('#hdnImagePath1').val((img_url == "" ? '' : that.getPath(img_url)));

                if (img_url == "")
                    $('#btn_stillcut').parent('li').removeClass("on");  //button off 처리
                else
                    $('#btn_stillcut').parent('li').addClass("on");  //button on 처리

                break;

            default:        //사용자 업로드
                $('#hdnImageType4').val((img_url == "" ? '-1' : '301'));
                $('#hdnImagePath4').val((img_url == "" ? '' : that.getPath(img_url)));
                $('#hdnImageDesc4').val('');
                type_code = "301";

                if (img_url == "")
                    $('#btn_upload').parent('li').removeClass("on");  //button off 처리
                else
                    $('#btn_upload').parent('li').addClass("on");  //button on 처리

                break;
        }

        if (type_code == "") return;

        //기존꺼 삭제
        for (var i = 0; i < choiceData.length; i++) {
            if (choiceData[i].typeCode == type_code) {
                choiceData.splice(i, 1);
            }
        }

        //신규 등록
        if (img_url != "") {
            var addData = { 'typeCode': type_code, 'imageURL': img_url };
            choiceData.push(addData);
        }
    }

    that.setUserChoice = function () {           //사용자가 선택한 3종셋트 display

        $('#layer_user_choice_item').empty();
        if (choiceData.length > 0) {
            $('#temp_user_choice_item').tmpl(choiceData).appendTo($('#layer_user_choice_item'));
            $('#layer_user_choice').show();
        } else {
            $('#layer_user_choice').hide();
        }

        $('#layer_user_choice_item .btn-del').on('click', that.removeItem);

    }

    that.removeItem = function (e) {  //item 한개 삭제
        that.setChoiceData($(this).val(), '', '');
        that.setUserChoice();
    }

    that.removeItemAll = function (e) {       //선택한 정보 모두 취소

        var targetData = choiceData.slice(0);   //삭제될 수 있으므로 대상객체 복사
        for (var i = 0; i < targetData.length; i++) {
            that.setChoiceData(targetData[i].typeCode, '', '');
        }

        //3종셋트 UI 재 셋팅
        that.setUserChoice();

        //모든 레이어 숨김
        $('.layer-wrap').remove();
    }

    that.getMovieItemList = function (e, type) {

        if (choiceMoveInfo.movieIdx == undefined || choiceMoveInfo.movieIdx < 1) {
            alert("영화를 먼저 선택하셔야 합니다.");
            return false;
        }

        switch (type) {
            case ('trailer'):
                app.movie().getMovieTrailerList({ movieIdx: choiceMoveInfo.movieIdx }, moviediary.setMovieTrailerList);
                break;
            case ('still'):
                app.movie().getMovieStillCutList({ movieIdx: choiceMoveInfo.movieIdx }, moviediary.setStillCutList);
                break;
        }
    }

    that.setMovieTrailerList = function (result) {

        //layout setting
        var $std = $('#btn_trailer'),
                    options = {
                        '$target': $std,
                        'html': $('#temp_layout_movie_multimedia').html(),
                        'position': 'position',
                        'mask': 'none'
                    };
        app.instWin.add(options);

        //item setting
        if ($('#watched_item_list')) {
            $('#temp_trailer').tmpl(result).appendTo($('#movie_item_list'));
        }

        $('#layout_movie_multimedia button').on('click', function () {      //trailer 선택
            var $this = $(this);
            that.setChoiceData('201', $this.data('image'), $this.val());
            $('#hdnImageGalleryIdx3').val($this.data("gallery-idx"));  // 동영상 galleryIdx Setting

            that.setUserChoice();       // UI Setting

            $('.layer-wrap').remove();      //선택 layer popup 삭제
        });

        //Layout 디자인스크롤 적용
        $('#layout_movie_multimedia').css({ width: 672, height: 400 }).customScrollbar();
        return false;
    }

    that.setStillCutList = function (result) {
        //layout setting
        var $std = $('#btn_trailer'),
                    options = {
                        '$target': $std,
                        'html': $('#temp_stillcut').html(),
                        'position': 'position',
                        'mask': 'none'
                    };
        app.instWin.add(options);

        var dataStillCut = [];
        //still cut image setting용 data
        for (var i = 0; i < result.length; i++) {
            var item = { 'galleryIdx': result[i].GalleryIdx
                    , 'movieIdx': result[i].MovieIdx
                    , 'imageUrl': result[i].ImageUrl
                    , 'thumbnailImageUrl': result[i].ThumnailImageUrl
                    , 'title': result[i].Title
            };
            dataStillCut.push(item);
        }

        //still cut
        $("#movie_item_list").tileGallery({ "data": dataStillCut
                                            , 'imageWidth': 224
                                            , 'leftMargins': [0, 234, 468]
                                            , 'limit': result.length
                                            , 'type': 'none'
                                            , 'callback': moviediary.tileGalleryBindAfterEventHandler
        });
    }

    that.tileGalleryBindAfterEventHandler = function (data) {

        if (data == undefined || data.length < 1) return;

        var $tId;
        for (var i = 0; i < data.length; i++) {

            $tId = $('#tile_' + i);
            if ($tId) {
                //app.log(data[i]);
                $tId.attr('data-image', data[i].imageUrl);
                $tId.attr('data-gallery-idx', data[i].galleryIdx);
                $tId.attr('title', data[i].title + '_스틸컷 선택');

                $tId.on('click', function (e) {

                    $this = $(this);

                    that.setChoiceData('101', $this.data('image'), '');
                    $('#hdnImageGalleryIdx1').val($this.data("gallery-idx"));  // 동영상 galleryIdx Setting
                    $('.layer-wrap').remove();      //선택 layer popup 삭제
                    that.setUserChoice();
                    return false;
                });
            }
        }


        //Layout 디자인스크롤 적용
        $('#layout_movie_multimedia').css({ width: 693, height: 400 }).customScrollbar();
    }

    that.getPath = function (url) {
        //도메인제거
        //app.log(url);
        if (url.indexOf('http://') >= 0)
            url = url.substring(url.indexOf('http://') + 7);

        return url.substring(url.indexOf('/'));
    }

    return that;
};
