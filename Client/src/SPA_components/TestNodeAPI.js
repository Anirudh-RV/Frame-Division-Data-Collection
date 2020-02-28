import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';


class TestAPI extends Component {
//TODO : ADD INTRODUCTION TO PROJECT


testdownloadapi = () =>{
  console.log("inside the testnodeapi function : ")
  axios.post("http://localhost:4000/download/",{
    username : 'sathyaswarupa',
    videoname : 'indiantraffic',
    videourl : 'https://www.youtube.com/watch?v=1Ap2G1Bfm0M'
  })
    .then(res => { // then print response status
      //toast.success('upload success')
      console.log(res)
    })
    .catch(err => {
    // then print response status
    //  toast.error('upload fail')
    console.log("fail")
    console.log(err)
    })
}

testdjangoapi = () =>{
  var username = 'anirudhrv'
  var videoname = 'testing'
  var imagetype = 'png'
  var videourl = 'http://localhost:4000/videos/'+username+'/downloads/'+videoname+'.mp4'
  var low = '1'
  var high = '5'
  var data = {'username':username,'videoname':videoname,'videourl':videourl,'imagetype':imagetype,'low':low,'high':high}
  console.log("inside the testdjangoapi function : ")
  axios.post("http://127.0.0.1:8000/index/",data)
    .then(res => { // then print response status
      //toast.success('upload success')
      console.log("API message : ")
      console.log(res)
      console.log(res.data["message"])
      if(this.DataRetrieved) {
       this.DataRetrieved.innerHTML = res.data["message"];
    }

    })
    .catch(err => { // then print response status
    //  toast.error('upload fail')
    console.log("fail")
    console.log(err)
    })
}


  render() {
    return (
      <div className="App">
      <h1>XP-2 TESTING API TO NODE, check developer tools for console.</h1>
      <pre>

      </pre>
      <button type="button" class="btn btn-success btn-block" onClick={this.testdownloadapi}> TEST DOWNLOAD OF VIDEO </button>
      <button type="button" class="btn btn-success btn-block" onClick={this.testdjangoapi}> TEST API TO DJANGO </button>

      <h1 className='name' ref = {c => this.DataRetrieved = c}></h1>
      </div>
    );
  }
}

export default TestAPI;
