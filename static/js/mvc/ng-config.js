 
'use strict';
var origin = window.location.origin;

var app = angular.module('angularApp', [
  'ui.router',
  'ngSanitize',
  'ngCookies'
  ])

app.config(function($sceDelegateProvider, $httpProvider) {  
  $sceDelegateProvider.resourceUrlWhitelist([
      // Allow same origin resource loads işi...
      'self',
      // Allow loading from our assets domain. 777 verir gibi hacı...
      origin+'/**',
      'https://player.vimeo.com/**',
      'https://www.youtube.com/**'
      ]);
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.withCredentials = true;
});

app.constant('ENDPOINTS', {
  api_endpoint: origin+'/api/',
  static_endpoint: origin+'/static/'
});

app.directive('csrfToken', function() {
  return {
    template: window.csrf_token
  };
});

app.directive('goClick', function($location) {
  return function(scope, element, attrs) {
    var path;
    attrs.$observe('goClick', function(val) {
      path = val;
    });
    element.bind('click', function() {
      scope.$apply(function() {
        $location.path(path);
      });
    });
  };
});

/*app.directive('tweenMaxStragger', function() {
    return function(scope, element, attrs) {
      var ease = Elastic.easeOut;
      TweenMax.staggerFrom(element.children(), 2, {
        scale: 0.7,
        opacity: 0,
        delay: 0.5,
        ease: ease
      }, 0.1);
    }
  })*/

  app.directive('tweenMaxStragger', function() {
    return function(scope, element, attrs) {
      var ease = Back.easeOut;
      TweenMax.staggerFrom(element.children(), 1, {
        scale: 0.6,
        opacity: 0,
        delay: 0,
        ease: ease
      }, 0.1);
    }
  })
  app.run(function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    })
/*
<ul tween-max-stragger>
    <li class="foo">A</li>
    <li class="foo">B</li>
    <li class="foo">C</li>
</ul>
*/