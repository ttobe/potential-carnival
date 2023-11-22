function fetchMemberJson() {
    fetch(`/user/islogin`)
        .then(response => response.json())
        .then((payload) => {
            document.getElementById("frame-1").innerHTML = ` <div class="button-small"><a href="/user/list.html">멤버리스트</a></div>
        <div class="button-small" id="nickname">${payload.nickname}</div>
        <div class="button-small" id="loginout"><a href="/user/logout">로그아웃</a></div>`
        })
        .catch(error => {
            document.getElementById("frame-1").innerHTML = `<div class="button-small" id="loginout"><a href="/user/login.html">로그인/회원가입</a></div>`
        });
}

fetchMemberJson();