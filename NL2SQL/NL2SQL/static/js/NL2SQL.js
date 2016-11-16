//Create a new AngularJS application
var app = angular.module('NL2SQLApp', []);

//Create a new controller in the AngularJS application
app.controller('NL2SQLController', function ($scope, $window, $http) {
    $scope.model = { NL_sentence: "", SQL_query: "" };

    //Function called when the Display SQL Query button is clicked
    $scope.getSQLQuery = function () {
        console.log("Here");
        //HTTP request to fetch SQL data from the server
        //Calls the backed Flask API
        $http({
            method: 'GET',
            params: { 'NL_sentence': $scope.model.NL_sentence },
            url: 'http://127.0.0.1:5557/getSQLQueryData'
        }).then(function mySucces(response) {
            console.log(response);
            $scope.model.SQL_query = response.data;
        }, function errorCallback(response) {
        });
    }

});


