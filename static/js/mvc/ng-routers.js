(function(){
  'use strict';
  app.config(function($stateProvider, $urlRouterProvider, $httpProvider, ENDPOINTS)
  {
    $stateProvider
    .state('main', {
      url: '/',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/main.html',
      controller:'mainCtrl'
    })
    .state('haberler', {
      url: '/haberler',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/haberler.html',
      controller:'haberlerCtrl'
    })
    .state('kurumsal', {
      url: '/kurumsal',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/kurumsal.html',
      controller:'kurumsalCtrl'
    })
    .state('geziler', {
      url: '/geziler',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/geziler.html',
      controller:'gezilerCtrl'
    })

    .state('gezi', {
      url: '/geziler/{path:.*}',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/gezi.html',
      controller:'geziCtrl'
    })

    .state('engelsiz-geziler', {
      url: '/engelsiz-geziler',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/engelsiz-geziler.html',
      controller:'engelsizCtrl'
    })

    .state('haber', {
      url: '/haberler/{path:.*}',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/haber.html',
      controller:'haberCtrl'
    })

    .state('sss', {
      url: '/sss',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/sss.html',
      controller:'sssCtrl'
    })
    .state('iletisim', {
      url: '/iletisim',
      templateUrl: ENDPOINTS.static_endpoint+'templates/ng_view/iletisim.html',
      controller:'iletisimCtrl'
    });

    $urlRouterProvider.otherwise("/");
  //$httpProvider.defaults.xsrfCookieName = 'csrftoken';
  //$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})

})();

