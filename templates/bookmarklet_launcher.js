(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(
            document.createElement('script')).
            src='https://592f3f52.ngrok.io/static/images/js/bookmarklet.js?r=' +
            Math.floor(Math.random()*99999999999999999999);
    }
})();