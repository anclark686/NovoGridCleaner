// Onclick of the button
document.getElementById("start-over").onclick = function () {  
    // Call python's random_python function
    eel.start_over()
    console.log("hello")
    document.getElementById('master-num').value=""
  }
