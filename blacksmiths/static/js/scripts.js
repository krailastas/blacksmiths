$(document).ready(function() {
	
	$("input[type='text'], input[type='tel'], input[type='email'], textarea").focus(function(){
		if(this.value==this.defaultValue){this.value=''};
		if($(this).hasClass('inp-error')) {
			$(this).removeClass('inp-error');
		}
	});
	$("input[type='text'], input[type='tel'], input[type='email'], textarea").blur(function(){
		if(this.value=='')this.value=this.defaultValue;
	});
	$("a[href='#']").click(function(e) {
		e.preventDefault();
	});
	$("[data-scroll]").click(function(e) {
		e.preventDefault();
		var toBlock = $(this).attr('data-scroll');
		var scrollTop = $(toBlock).offset().top;
		$('body,html').animate({scrollTop: scrollTop}, 1200);
	});
	$("[data-link]").click(function(e) {
		var link = $(this).attr('data-link');
		window.open(link, '_self');
	});

	// Анкоры в меню
	$("#menu li a").click(function(e) {
		var toBlock = $(this).attr('href');
		if(toBlock.substr(0,1)=='#') {
			e.preventDefault();
			if($('body').find(toBlock).is(toBlock)) {
				var scrollTop = $(toBlock).offset().top;
				$('body,html').animate({scrollTop: scrollTop}, 1500);
			} else {
				window.open(location.protocol+'//'+location.host+'/'+toBlock, '_self');
			}
		}
	});

	// Модальные окна
	$("[data-modal]").click(function(e) {
		e.preventDefault();
		var modalID = $(this).attr('data-modal');
		$('#'+modalID).arcticmodal({closeOnEsc:true,closeOnOverlayClick:true});
	});

//	// Модальные окна (материалы)
//	$("#material-partners .material-item").click(function(e) {
//		e.preventDefault();
//		var that = $(this);
//		var modalTitle = that.find('.zag').text();
//		var modalContent = that.find('.desc').html();
//		$('#Modal-material .zagolovok').text(modalTitle);
//		$('#Modal-material .txt-wrap').html(modalContent);
//		$('#Modal-material').arcticmodal({closeOnEsc:true,closeOnOverlayClick:true});
//	});
//	$(".material-modal").on("click", '.button-yellow', function(e) {
//		e.preventDefault();
//		$.arcticmodal('close');
//		var that = $(this);
//		var modalTitle = that.text();
//		$('#Modal-material-single .form-title').val(modalTitle);
//		$('#Modal-material-single .submit-button').val(modalTitle);
//		$('#Modal-material-single').arcticmodal({closeOnEsc:true,closeOnOverlayClick:true});
//	});

	// Услуги (смена картинок)
	$('#uslugi .item > span').click(function(e) {
		e.preventDefault();
		$(this).parents('#uslugi').find('.item').removeClass('active');
		var that = $(this).parents('.item');
		var img = $('#uslugi .img > img');
		that.addClass('active');
		img.removeClass('left right');
		if(that.hasClass('left')) {
			img.addClass('left');
		} else if(that.hasClass('right')) {
			img.addClass('right');
		}
		var new_src = that.attr('data-img');
		img.attr('src', 'images/uslugi/'+new_src+'.png');
	});

	// Таймер
	var dateYear = 2025;
	var dateMonth = 1;
	var dateDay = 1;
	var lastDay = new Date(parseInt(dateYear), parseInt(dateMonth-1), parseInt(dateDay));
	$('#defaultCountdown').countdown({until: lastDay, layout: '<div class="time hours">{hnn}</div><div class="time minutes">{mnn}</div><div class="time sec">{snn}</div>'});

	// Фансибокс
	$("a[rel='gallery'], .fancybox").fancybox({
		'speedIn'   : 500,
		'speedOut'  : 400,
		'maxWidth'  : 1200,
		'maxHeight' : 600,
		'helpers'   : {'overlay':{'locked':false}}
	});

	// Добавить комментарий
	$('#defects .add-comment > span').click(function(e) {
		e.preventDefault();
		var that = $(this);
		var root = that.parents('.add-comment');
		if(root.hasClass('active')) {
			root.removeClass('active');
			root.parent().find('.comment').addClass('hidden');
		} else {
			root.addClass('active');
			root.parent().find('.comment').removeClass('hidden');
		}
		root.find('.comment').val('');
	});

	// Слайдер работ
	var works = $('#owl-works');
	works.owlCarousel({
		items: 4,
		dots: false,
		loop: true,
		margin: 0,
		smartSpeed: 600,
		nav: false,
		mouseDrag: false,
		navText: ['',''],
		responsive:{
			0:{ items: 1 },
			800:{ items: 2 },
			1200:{ items: 4 }
		}       
    });
	$('#works .wrap span.arrows.prev').click(function(e) {
		e.preventDefault();
		works.trigger('prev.owl.carousel');
	});
	$('#works .wrap span.arrows.next').click(function(e) {
		e.preventDefault();
		works.trigger('next.owl.carousel');
	});

	// Слайдер отзывов
	var reviews = $('#owl-reviews');
	reviews.owlCarousel({
		items: 1,
		dots: false,
		loop: true,
		margin: 0,
		smartSpeed: 600,
		nav: false,
		mouseDrag: false,
		navText: ['','']     
    });
	$('#reviews .wrap span.arrows.prev').click(function(e) {
		e.preventDefault();
		reviews.trigger('prev.owl.carousel');
	});
	$('#reviews .wrap span.arrows.next').click(function(e) {
		e.preventDefault();
		reviews.trigger('next.owl.carousel');
	});

	// Отправка форм заявок
	var errorText = 'Простите, но сервер не смог отправить вашу заявку. Попробуете ещё раз, пожалуйста.';
	var ok=0;
	var options = { 
		clearForm: true,
		resetForm: true,
		success: function(data) {
			if(data=='ok') {
				window.open('thanks.php', '_self');
				$('body').find(".inps").removeClass('inp-error').val(''); 
				ok=0;
				$.arcticmodal('close'); 
			} else {
				alert(errorText);
			}
		},
		error: function() {}	
	};
	$("form").submit(function(e) {
		// e.preventDefault();
		// e.stopPropagation();
		var error = 0;
		$(this).find(".inps").removeClass('inp-error');
		if($(this).find("input").is(".name")) {
			var name = $(this).find(".name");
			if(name.hasClass('required')) {
				if(name.val().length<=2) {
					name.addClass('inp-error');
					error=1;
				}
			}
		}
		if($(this).find("input").is(".phone")) {
			var phone = $(this).find(".phone");
			if(phone.hasClass('required')) {
				if(ok==0) {
					phone.addClass('inp-error');
					error=1;
				}
			}
		}	
		if($(this).find("input").is(".email")) {
			var email = $(this).find(".email");
			if(email.hasClass('required')) {
				if(!email.val().match(/^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$/)) {
					email.addClass('inp-error');
					error=1;
				}
			}
		}
		if($(this).find("textarea").is(".comment")) {
			var comment = $(this).find(".comment");
			if(comment.hasClass('hidden')) {
				comment.val('');
			} else {
				if(comment.hasClass('required')) {
					if(!comment.val().length<=5) {
						comment.addClass('inp-error');
						error=1;
					}
				}	
			}
		}
		if(error==1) {
			return false;
		}
		// $(this).ajaxSubmit(options);
	});

    // Placeholder
    $('input, textarea').placeholder();
	
	// Маски поля
	$(".phone_field").mask("+38 (999) 999-99-99",{completed:function(){ok=1}});

	// Параллакс
	$('[data-parallax]').parallaxFenesko();
   
	// Анимация
	$('.animate').scrolla();

});