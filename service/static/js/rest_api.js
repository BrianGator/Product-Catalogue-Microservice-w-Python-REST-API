$(function () {

    function update_form_data(res) {
        $("#product_id").val(res.id);
        $("#product_name").val(res.name);
        $("#product_description").val(res.description);
        $("#product_price").val(res.price);
        if (res.available == true) {
            $("#product_available").val("True");
        } else {
            $("#product_available").val("False");
        }
        $("#product_category").val(res.category);
    }

    function flash_message(message) {
        $("#flash_message").empty();
        $("#flash_message").append(message);
    }

    $("#clear-btn").on("click", function () {
        $("#product_id").val("");
        $("#product_name").val("");
        $("#product_description").val("");
        $("#product_price").val("");
        $("#product_available").val("True");
        $("#product_category").val("UNKNOWN");
        flash_message("Cleared");
    });

    $("#create-btn").on("click", function () {
        let name = $("#product_name").val();
        let description = $("#product_description").val();
        let price = $("#product_price").val();
        let available = $("#product_available").val() == "True";
        let category = $("#product_category").val();

        let data = {
            "name": name,
            "description": description,
            "price": price,
            "available": available,
            "category": category
        };

        let ajax = $.ajax({
            type: "POST",
            url: "/products",
            contentType: "application/json",
            data: JSON.stringify(data),
        });

        ajax.done(function (res) {
            update_form_data(res);
            flash_message("Success");
        });

        ajax.fail(function (res) {
            flash_message(res.responseJSON.message);
        });
    });

    $("#retrieve-btn").on("click", function () {
        let product_id = $("#product_id").val();

        let ajax = $.ajax({
            type: "GET",
            url: "/products/" + product_id,
            contentType: "application/json",
            data: ''
        });

        ajax.done(function (res) {
            update_form_data(res);
            flash_message("Success");
        });

        ajax.fail(function (res) {
            flash_message("404 Not Found");
        });
    });

    $("#update-btn").on("click", function () {
        let product_id = $("#product_id").val();
        let name = $("#product_name").val();
        let description = $("#product_description").val();
        let price = $("#product_price").val();
        let available = $("#product_available").val() == "True";
        let category = $("#product_category").val();

        let data = {
            "name": name,
            "description": description,
            "price": price,
            "available": available,
            "category": category
        };

        let ajax = $.ajax({
            type: "PUT",
            url: "/products/" + product_id,
            contentType: "application/json",
            data: JSON.stringify(data)
        });

        ajax.done(function (res) {
            update_form_data(res);
            flash_message("Success");
        });

        ajax.fail(function (res) {
            flash_message(res.responseJSON.message);
        });
    });

    $("#delete-btn").on("click", function () {
        let product_id = $("#product_id").val();

        let ajax = $.ajax({
            type: "DELETE",
            url: "/products/" + product_id,
            contentType: "application/json",
            data: '',
        });

        ajax.done(function (res) {
            $("#clear-btn").click();
            flash_message("Product has been Deleted!");
        });

        ajax.fail(function (res) {
            flash_message("Server error!");
        });
    });

    $("#search-btn").on("click", function () {
        let name = $("#product_name").val();
        let category = $("#product_category").val();
        let available = $("#product_available").val();

        let queryString = "";

        if (name) {
            queryString += 'name=' + name;
        }
        if (category && category != "UNKNOWN") {
            if (queryString.length > 0) {
                queryString += '&category=' + category;
            } else {
                queryString += 'category=' + category;
            }
        }
        if (available) {
            if (queryString.length > 0) {
                queryString += '&available=' + available;
            } else {
                queryString += 'available=' + available;
            }
        }

        let ajax = $.ajax({
            type: "GET",
            url: "/products?" + queryString,
            contentType: "application/json",
            data: ''
        });

        ajax.done(function (res) {
            $("#search_results tbody").empty();
            let table = "";
            for (let i = 0; i < res.length; i++) {
                let product = res[i];
                let row = "<tr><td>" + product.id + "</td><td>" + product.name + "</td><td>" + product.description + "</td><td>" + product.price + "</td><td>" + product.available + "</td><td>" + product.category + "</td></tr>";
                $("#search_results tbody").append(row);
            }
            flash_message("Success");
        });

        ajax.fail(function (res) {
            flash_message(res.responseJSON.message);
        });
    });

});
