let time_obj = undefined;
let flag = undefined;
let chars = undefined;
let result_flag = false;

window.onload = () => {
    time_obj = document.getElementById("timer");
    flag = false;       // 더블 클릭 체크
}

function double_submit_check() {
    if (flag) {
        console.log("double");
        return true;
    }
    else {
        flag = true;
        return false;
    }
}

function context_changed(value){
    if(value.replace(/ /g,"") == ""){
        document.getElementById("word_count").innerHTML = "words: " + 0;
        return;
    }
    var words = value.split(" ");
    if(words[words.length - 1] == ""){
        words.pop();
    }
    document.getElementById("word_count").innerHTML = "words: " + words.length;

    let items = document.getElementsByClassName("item form-control");
    if(result_flag){
        for (var i = 0; i<items.length; i++){
            items[i].style.background = "white";
        }
        result_flag = false;
    }
}

function send_req() {
    let items = document.getElementsByClassName("item form-control");
    let context = document.getElementById("context");
    let result = document.getElementById("result");
    const formData = new FormData();
    const url = "/generate";
    let items_value = Array();

    for (var i = 0; i<items.length; i++){
        items_value.push(items[i].value);
    }

    if (double_submit_check()){
        return ;
    }

    if ( context.value == '') {
        document.getElementById('warning').innerText = 'Please fill text!';
        flag = false;
        return ;
    }

    let start = 0;
    
    formData.append('context', context.value);

    // timer
    timer = setInterval(() => {
        start += 1;
        time_obj.innerText = `${start / 10} 's`;
    }, 100);

    fetch (url, { method: 'POST', body: formData, })
    .then(response => {
        if (response.status === 200) {
            return response.json();
        } else {
            clearInterval(timer);
            flag = false;
        }
    }).catch(err => {
        clearInterval(timer);
        flag = false;
        document.getElementById('warning').innerText = err;
    }).then(data => {
        let result_sentece = "";
        result_sentece = data["label"]
        alert(result_sentece)
        clearInterval(timer);
        time_obj.innerText = 'Done!';
        flag = false;
        for (var i = 0; i<items.length; i++){
            if(items[i].value == result_sentece){
                items[i].style.background = "lightgreen";
                result_flag = true;
            }
        }
    }).catch(err => {
        clearInterval(timer);
        flag = false;
        document.getElementById('warning').innerText = err;
    });
}