// http://angulartutorial.blogspot.com/2014/03/rating-stars-in-angular-js-using.html

(function() {
  'use strict';

  angular
    .module('app', [])
    .controller('RatingController', RatingController)
    .directive('starRating', starRating);

  function RatingController($scope, $http, $location) {
    $scope.target_name="&"
    $scope.total=0
    $scope.user=""
    $scope.isReadonly=true;
    $scope.target_id=$location.search().id;
    $scope.checks=""
    get_name($scope)
    get_conf($scope)

      function get_name($scope){
      $http({
        method  : 'GET',
        url     : '/user/show/' + $scope.target_id,
       })
        .success(function(data) {
          $scope.target_name = data
        });
      }

    function get_conf($scope){
        $http({
          method  : 'GET',
          url     : '/config/list',
         })
          .success(function(data) {
            $scope.checks = angular.fromJson(data)
          });
        }

      $scope.savescore = function(user, target, checks) {
        // Posting data to php file
        $http({
          method  : 'POST',
          url     : "/score/add/" + user + "/" + target,
          data    : angular.toJson(checks), //forms user object
          headers : {'Content-Type': 'application/json'}
         })
          .success(function(data) {
            if (data.errors) {
              // Showing errors.
            } else {
            }
          });
        };


    $scope.rateFunction = function(checks) {

         var total_score = 0;
          for (var i=0; i < checks.length; i++) {
              total_score += Number(checks[i].rating);
          }
        $scope.total=total_score
    };
    $scope.rateFunction($scope.checks)
  }

  function starRating() {
    return {
      restrict: 'EA',
      template:
        '<ul class="star-rating" ng-class="{readonly: readonly}">' +
        '  <li ng-repeat="star in stars" class="star" ng-class="{filled: star.filled}" ng-click="toggle($index)">' +
        '    <i class="fa fa-star"></i>' + // or &#9733
        '  </li>' +
        '</ul>',
      scope: {
        ratingValue: '=ngModel',
        totle_fn: '=func',
        args:'=arg',
        max: '=?', // optional (default is 5)
        onRatingSelect: '&?',
        readonly: '=?'
      },
      link: function(scope, element, attributes) {
        if (scope.max == undefined) {
          scope.max = 5;
        }
        function updateStars() {
          scope.stars = [];
          for (var i = 0; i < scope.max; i++) {
            scope.stars.push({
              filled: i < scope.ratingValue
            });
          }
        };
        scope.toggle = function(index) {
          if (scope.readonly == undefined || scope.readonly === false){
            scope.ratingValue = index + 1;
            scope.onRatingSelect({
              rating: index + 1
            });
          }
        };
        scope.$watch('ratingValue', function(oldValue, newValue) {
          if (newValue) {
            updateStars();
            scope.totle_fn(scope.args)
          }
        });
      }
    };
  }
})();