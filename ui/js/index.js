// http://angulartutorial.blogspot.com/2014/03/rating-stars-in-angular-js-using.html

(function() {
  'use strict';

  angular
    .module('app', [])
    .controller('RatingController', RatingController)
    .directive('starRating', starRating);

  function RatingController($http) {
    this.myname="Â½¿µ"
    this.user=""
    this.isReadonly = true;
      this.checks=[{
              id: "01",
              name_cn: "Ë§Æø",
              name_en: "handsome",
              desc_cn: "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              desc_en: "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              score: "5",
              rating: "2"
            }, {
              id: "02",
              name_cn: "¾­¼Ã",
              name_en: "emkkk",
              desc_cn: "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              desc_en: "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              score: "5",
              rating: "2"
            }
      ]
      this.submitForm = function() {
        // Posting data to php file
        $http({
          method  : 'POST',
          url     : 'save/' + this.user,
          data    : angular.toJson(this.checks), //forms user object
          headers : {'Content-Type': 'application/json'}
         })
          .success(function(data) {
            if (data.errors) {
              // Showing errors.
            } else {
            }
          });
        };

    this.rateFunction = function(rating) {
      console.log('Rating selected: ' + rating);
    };
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
          }
        });
      }
    };
  }
})();