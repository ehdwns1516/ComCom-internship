let time_obj = undefined;
let flag = undefined;
let chars = undefined;

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
}

function change_num_beams(value){
    document.getElementById("label_num_beams").innerHTML="# beam search: " + value;
    console.log(value);

}
function change_max_words(value){
    document.getElementById("label_max_words").innerHTML="# max words in summary: " + value;
}
function change_min_words(value){
    document.getElementById("label_min_words").innerHTML="# min words in summary: " + value;
}

function send_req() {
    let max_words = document.getElementById("max_words");
    let min_words = document.getElementById("min_words");
    let num_beams = document.getElementById("num_beams");
    let context = document.getElementById("context");
    let result = document.getElementById("result");

    if (double_submit_check()){
        return ;
    }

    if ( context.value == '') {
        document.getElementById('warning').innerText = 'Please fill text!';
        flag = false;
        return ;
    }

    const formData = new FormData();
    const url = "/generate";
    let start = 0;

    formData.append('max_words', max_words.value);
    formData.append('min_words', min_words.value);
    formData.append('num_beams', num_beams.value);
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
        let summary = "";
        for(var i in data){
            summary += (i + ": " + data[i] + "\n");
        }

        result.innerHTML = summary;
        clearInterval(timer);
        time_obj.innerText = 'Done!';
        flag = false;

    }).catch(err => {
        clearInterval(timer);
        flag = false;
        document.getElementById('warning').innerText = err;
    });
}