const hide = el => el.style.display = 'none';
const show = el => el.style.display = 'block';
const get_token = () => localStorage.getItem("jwt_token");

const login = document.getElementById("login");
const reg = document.getElementById("reg");
const info = document.getElementById("info");
const error = document.getElementById("error");

const reg_button = document.getElementById("reg_button");
const login_button = document.getElementById("log_button");
const logout_button = document.getElementById("logout_button");

hide(login);
hide(reg);
hide(error);
hide(info);
hide(reg_button);
hide(login_button);
hide(logout_button);

if(get_token()){
    
}