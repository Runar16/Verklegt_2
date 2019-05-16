function emptyCart() {
        let total = document.getElementById("total").innerText;
        let buttonsToHide = document.getElementsByClassName("btn btn-success");
        if (total === "0"){
            document.getElementById("emptyCart").style.display = "block";
            for(let i = 0; i < buttonsToHide.length; i++){
                buttonsToHide[i].innerText = "Find properties";
                buttonsToHide[i].setAttribute("onclick", "window.location.href = '{% url 'frontpage' %}'");
                buttonsToHide[i].style.display = "inline-block";
    }
        } else {
            for(let i = 0; i < buttonsToHide.length; i++){
                buttonsToHide[i].style.display = "inline-block";
    }
        }
    }