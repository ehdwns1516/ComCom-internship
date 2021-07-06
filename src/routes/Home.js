import React, { Component } from "react";
import './Home.css'

export default class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            context: "",
            textSize: 0
        }
    }

    handleConentChange = (e) => {
        this.setState({
            context: e.target.value,
            textSize: e.target.value.length
        })
    }

    request_api = (text) => {
        fetch('https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/preprocess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=\'utf-8\''
            },
            body: JSON.stringify({
                "context": text
            })
        }).then(response => response.text()).then(response => {
            response = response.replace(/\[/g, '');
            response = response.replace(/\]/g, '');
            response = response.replace(/\"/g, '');
            let vecArr = response.split(", ")
            const vecArr_int = vecArr.map((i) => Number(i));
            fetch('https://train-95y6kshrdyxtj652igs7-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-en-small-finetune', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json; charset=\'utf-8\''
                },
                body: JSON.stringify({
                    "text": vecArr_int,
                    "num_samples": 1,
                    "length": 50
                })
            }).then(response => response.json()).then(response => {
                fetch('https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/postprocess', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(
                        response
                    )
                }).then(response => response.text()).then(response =>{
                    if (response !== null) {
                        let vervse = response.substr(14, response.length)
                        vervse = vervse.replace(/\}/g, '');
                        vervse = vervse.replace(/\"/g, '');
                        this.setState({
                            context: vervse,
                            textSize: vervse.length
                        })
                        document.querySelector(".textarea_context").value = this.state.context;
                    }
                    else {
                        alert("api request failed.");
                    }
                })
            })
        })
    }

    submit_makeReview = () => {
        if (this.state.context === "") {
            this.request_api("he");
        }
        else {
            this.request_api(this.state.context);
        }

    }

    render = () => {
        return (
            <div className="mainContent">
                <h1 style={{ fontSize: "40px", marginTop: "50px" }}>Bible Verse Generator(English)</h1>
                <div style={{ display: "flex", justifyContent: "center", marginTop: "60px" }}>
                    <textarea className="textarea_context" placeholder="Input keyword of Bible." onChange={this.handleConentChange}></textarea>
                    <button className="button_submit" onClick={this.submit_makeReview}>Make Verse!</button>
                </div>
                <span className="textSize" style={{ justifyContent: "space-between" }}>text size: {this.state.textSize}</span>
            </div>
        )
    }
}