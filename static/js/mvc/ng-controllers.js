;(function(){
//  ----- ========= MAIN CONTROLLERS ======== -----

app.controller('mainCtrl',
 ['$scope', '$http','$log', 'ENDPOINTS',

 function($scope, $http, $log, ENDPOINTS) {

  (function(){
   $('#geziler-landing').show(500);

   $('.video-trigger').click(function(e){
     e.preventDefault();
     $('body').addClass('overflow_hidden');
     let idModal = $(this).attr('click');
     console.log(idModal+' tıklandı');
     let targetModal = $('.'+idModal);
     let vid = targetModal.find('#' + idModal);

     TweenLite.to(targetModal, 0.9,
      {top: 0, ease:Power2.easeInOut});
     TweenLite.to($('.' + idModal + ' .close-video'), 0.7,
      {marginTop: '0px', opacity: 1, delay:0.6, ease:Power2.easeInOut} );
     setTimeout(function(){
     }, 750);

     $('.close-video').click(function(e){
      e.preventDefault();
      $('body').removeClass('overflow_hidden');
      let idModalClose = $(this).attr('id');
      let targetModalClose = $('.'+idModalClose);

      TweenLite.to($('.' + idModalClose + ' .close-video'), 0.5,
       {marginTop: '30px', opacity: 0, ease:Power2.easeInOut});
      TweenLite.to(targetModalClose, 0.7,
       {top: '110%', delay:0.4, ease:Power2.easeInOut});
          })//close modal sonu

     $('.close-modal').click(function(e){
      e.preventDefault();
      $('body').removeClass('overflow_hidden');
      let idModalClose = $(this).attr('id');
      let targetModalClose = $('.'+idModalClose);

      TweenLite.to($('.' + idModalClose + ' .close-video'), 0.5,
       {marginTop: '30px', opacity: 0, ease:Power2.easeInOut});
      TweenLite.to(targetModalClose, 0.7,
       {top: '110%', delay:0.4, ease:Power2.easeInOut});
          })//close modal sonu
      }) // videotrigger click
 })();

 $("#fail").hide();
 $("#success").hide();
 $scope.rotalar = $http.get(ENDPOINTS.api_endpoint+'rotalar/').then(function(response){
   $scope.rotalar = response.data
   $log.info($scope.rotalar)
 })
}
	 ]//injection sonu
	); //controller sonu


app.controller('haberlerCtrl',
 ['$scope', '$http','$log', 'ENDPOINTS',

 function($scope, $http, $log, ENDPOINTS) {
  $("#fail").hide();
  $("#success").hide();

  $scope.haberler = $http.get(ENDPOINTS.api_endpoint+'haberler/').then(function(response){
   $scope.haberler = response.data
   $log.info($scope.haberler)
 })
}
	 ]//injection sonu
	); //controller sonu

app.controller('kurumsalCtrl',
 ['$scope', '$http','$log', 'ENDPOINTS',

 function($scope, $http, $log, ENDPOINTS) {
  $('#geziler-landing').hide();
  $("#container-layer").show(600);
  $("#fail").hide();
  $("#success").hide();
  $scope.kurumsal = $http.get(ENDPOINTS.api_endpoint+'sayfa/1/').then(function(response){
   $scope.kurumsal = response.data
   $scope.kurumsalHTML = $scope.kurumsal.icerik
   $log.info($scope.kurumsal)
 })
}
	 ]//injection sonu
	); //controller sonu


app.controller('gezilerCtrl',
 ['$scope', '$http','$log', 'ENDPOINTS',

 function($scope, $http, $log, ENDPOINTS) {
  $("#fail").hide();
  $("#success").hide();
  $scope.geziler = $http.get(ENDPOINTS.api_endpoint+'rotalar/').then(function(response){
   $scope.geziler = response.data
   $log.info($scope.geziler)
 })
}
	 ]//injection sonu
	); //controller sonu

app.controller('geziCtrl',
  ['$scope', '$http','$log', 'ENDPOINTS',

  function($scope, $http, $log, ENDPOINTS) {
    $("#fail").hide();
    $("#success").hide();

    let hash = document.location.hash;
    $scope.splitted = hash.split("&=");

    $scope.gezi = $http.get(ENDPOINTS.api_endpoint+'rotalar/'+$scope.splitted[1]+'/').then(function(response){
      $scope.gezi = response.data;
      $scope.contextHTML = $scope.gezi.icerik;
        // id yi aldıktan sonra videolar için tekrar Endpoint e gidiyoruz.
      $scope.gezi_video = $http.get(ENDPOINTS.api_endpoint+'rotalar/videolar/'+$scope.gezi.id).then(function(res){
          $scope.gezi_video = res.data;
          $log.info($scope.gezi_video);

          $scope.gezi_video.forEach( function(element, index) {
        $(".videoRepeat").append(
          '<li class="col-sm-6 col-xs-12 wow fadeInUp" style="margin-top:20px;">' +
            '<div class="embed-responsive embed-responsive-16by9">'+element.video_url+'</div></li>'
          );
      }); //foreach sonu

      })//video request sonu


        $scope.gezi_foto = $http.get(ENDPOINTS.api_endpoint+'rotalar/fotograflar/'+$scope.gezi.id).then(function(res){
          $scope.gezi_foto = res.data;
          $log.info($scope.gezi_foto);
      })//video request sonu

    })

  }]);

app.controller('engelsizCtrl', 
 ['$scope', '$http','$log', 'ENDPOINTS',

 function($scope, $http, $log, ENDPOINTS) {
  $("#fail").hide();
  $("#success").hide();
  $scope.engelsiz_rotalar = $http.get(ENDPOINTS.api_endpoint+'rotalar/kategori/7/').then(function(response){
   $scope.engelsiz_rotalar = response.data
   $log.info($scope.engelsiz_rotalar)
 })
}
	 ]//injection sonu
	); //controller sonu


app.controller('haberCtrl', 
  ['$scope', '$http','$log', 'ENDPOINTS',

  function($scope, $http, $log, ENDPOINTS) {


    $('html, body').animate({scrollTop: $("#container-layer").offset().top-20}, 300);


    $("#fail").hide();
    $("#success").hide();

    let hash = document.location.hash;
    $scope.splitted = hash.split("&=");

    $scope.context = $http.get(ENDPOINTS.api_endpoint+'haberler/'+$scope.splitted[1]+'/').then(function(response){
      $scope.context = response.data
      $scope.contextHTML = $scope.context.icerik 
    })

  }]);

app.controller('sssCtrl', 
 ['$scope', '$http','$log', 'ENDPOINTS',

 function($scope, $http, $log, ENDPOINTS) {
   $("#fail").hide();
   $("#success").hide();
   $scope.sss = $http.get(ENDPOINTS.api_endpoint+'sayfa/2/').then(function(response){
     $scope.sss = response.data
     $scope.sssHTML = $scope.sss.icerik 
     $log.info($scope.sss)
   })
 }
	 ]//injection sonu
	); //controller sonu

app.controller('iletisimCtrl', 
  ['$scope','$rootScope', '$http','$log','$filter','$location', 'ENDPOINTS',

  function($scope, $rootScope, $http, $log,$filter,$location, ENDPOINTS) {
   $("#success-form").hide();  
   $("#gonder_btn").text("Mesajı Gönder");
   $("#fail-form").hide();
   $("#fail").hide();
   $("#success").hide();
   $scope.submitForm = function(data, ad_soyad, email, mesaj) {

    $("#gonder_btn").html('Gönderiliyor... <img src="static/images/puff.svg" alt="">')
    $scope.ad_soyad = this.ad_soyad
    $scope.email = this.email
    $scope.mesaj = this.mesaj
    $scope._csrf = $("[name=csrfmiddlewaretoken]").val();

     $scope.data = {
         ad_soyad: $scope.ad_soyad,
        email: $scope.email,
        mesaj: $scope.mesaj

      };
      let iletisimReq = {
       method: 'POST',
       url: ENDPOINTS.api_endpoint+'iletisim/',
       headers:{
        'X-CSRFToken':$scope._csrf
       },
       data: $scope.data
     }
     //$http(req).then(function(){...}, function(){...});
      
  
      $scope.iletisim = $http(iletisimReq).then(function(response){
        $scope.iletisim = response.data
        $log.info($scope.iletisim)
        $("#successMessage").text("Mesajınız Başarı ile kaydedildi.")
        $("#contact-form").hide(100,function(){
          $("#success-form").show();  
          $("#gonder_btn").text("Mesajı Gönder");
          $("#fail-form").hide();
        });

        $("#success").slideDown(200,function(){
          $("#success").delay(4000).slideUp(200);
        });


      },function(error){
        $log.info(error.data.detail);
        $("#errorMessage").text(error.data.detail)
        $("#errorMessageTop").text(error.data.detail)
        $("#gonder_btn").text("Mesajı Gönder");
        $("#fail-form").show();
        $("#fail").slideDown(200,function(){
          $("#fail").delay(4000).slideUp(200);
        });
          //$("#gonder_btn").css('background-color', 'red');
        })

    
  };  

}]);

app.controller('basvurCtrl', 
  ['$scope', '$http','$log', 'ENDPOINTS','$cookies',

  function($scope, $http, $log, ENDPOINTS, $cookies) {
   $("#modal_basvuru_sonucu").hide();  
   $("#gonder_btn2").text("Mesajı Gönder");
   $("#fail-form2").hide();
   $("#fail").hide();
   $("#success").hide();
   $scope.kategori = $http.get(ENDPOINTS.api_endpoint+'rotalar/kategoriler/').then(function(response){
     $scope.kategori = response.data
     $log.info($scope.kategori)
   })

   $scope.submitBasvurForm = function(data, ad_soyad, email, mesaj, basTuru, telefon, katBaslik) {

    $scope.ad_soyad = this.ad_soyad
    $scope.email = this.email
    $scope.katBaslik = this.katBaslik
    $scope.basTuru = this.basTuru || "Grup"
    $scope.mesaj = this.mesaj
    $scope.telefon = this.telefon.toString();


    $scope._csrf = $("[name=csrfmiddlewaretoken]").val();
    /*document.cookie = "csrftoken="+_csrf+";";
    $cookies.csrftoken = _csrf;
    $log.info($cookies.csrftoken);*/

      $scope.data = {
        ad_soyad: $scope.ad_soyad,
        email: $scope.email,
        mesaj: $scope.mesaj,
        gezi_turu: $scope.katBaslik,
        basvuru_turu: $scope.basTuru,
        tel_no:$scope.telefon,

      };
      let req = {
       method: 'POST',
       url: ENDPOINTS.api_endpoint+'basvur/',
       headers:{
        'X-CSRFToken':$scope._csrf
       },
       data: $scope.data
     }
     //$http(req).then(function(){...}, function(){...});
      $scope.basvur = $http(req).then(function(response){
        $scope.basvur = response.data
        
        $("#modal_basvuru_sonucu").css({
          opacity: '1',
          display: 'block',
          transform: 'translate(0%, 0%) matrix(1, 0, 0, 1, 0, 0)'
        });

        $("#successMessage").text("Mesajınız Başarı ile kaydedildi.")
        $("#modal_form").slideUp(100,function(){
          $("#modal_basvuru_sonucu").show();  
          $("#gonder_btn2").text("Mesajı Gönder");
          $("#fail-form2").hide();
        });

        $("#success").slideDown(500,function(){
          $("#success").delay(4000).slideUp(200);
        });


      },function(error){
        $log.info(error.data[0]);
        $("#fail-form2").show();
        $("#gonder_btn").text("Mesajı Gönder");
        
        if(error.status === 403){
          $("#errorMessage2").text("CSRF Hatası")
          $("#errorMessageTop").text("CSRF Hatası")  
        }
        else
        {
          $("#errorMessage2").text(error.data.detail)
          $("#errorMessageTop").text(error.data.detail)
        }
        
        $("#fail").slideDown(200,function(){
          $("#fail").delay(4000).slideUp(200);
        });
      })
    
  }; 


}]);

  })();	