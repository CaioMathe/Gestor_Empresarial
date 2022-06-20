{% extends 'base.html' %} 
{% block content %}

{% load crispy_forms_tags %}
<style>
input{
  width: 50%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
  
}
.campos{
    margin-left: 30%;
}
.div_btn{
    margin-left: 38%;
}
.links{
  background-color: white;
  border-radius: 6px;
  width: 40px;
  height: 40px;
}
.fa-user-tie{
  color: rgb(24, 26, 24);
  margin-top:5px;
  margin-left:5px;
}
.id_empresa{
    width: 100px;
}
.btn, .btn-retornar{
  align-items: center;
  appearance: none;
  background-color: #fff;
  border-radius: 24px;
  border-style: none;
  box-shadow: rgba(0, 0, 0, .2) 0 3px 5px -1px,rgba(0, 0, 0, .14) 0 6px 10px 0,rgba(0, 0, 0, .12) 0 1px 18px 0;
  box-sizing: border-box;
  color: #3c4043;
  cursor: pointer;
  display: inline-flex;
  fill: currentcolor;
  font-family: "Google Sans",Roboto,Arial,sans-serif;
  font-size: 14px;
  font-weight: 500;
  height: 48px;
  justify-content: center;
  letter-spacing: .25px;
  line-height: normal;
  max-width: 100%;
  overflow: visible;
  padding: 2px 24px;
  position: relative;
  text-align: center;
  text-transform: none;
  transition: box-shadow 280ms cubic-bezier(.4, 0, .2, 1),opacity 15ms linear 30ms,transform 270ms cubic-bezier(0, 0, .2, 1) 0ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: auto;
  will-change: transform,opacity;
  z-index: 0;
}
.btn-retornar:hover{
  background:  rgb(255, 0, 0);
  color: #ffffff;
}
.btn:hover {
  background:  rgb(0, 255, 98);
  color: #ffffff;
}
.cadata{
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: auto;
}
hr{
    margin-bottom: 30px;
}
</style>

<div class="thumbnail"></div>
<div class="ml-5 mr-5">
  <form action="" method="POST" autocomplete="off">
    {% csrf_token %}

    {% crispy form %}
  </form>
</div>

<script>
    window.onload = function  (){
        document.getElementById('id_id_empresa').readOnly = true; 
        document.getElementById('id_id_empresa').value = geraStringAleatoria(5)
    }
    

    function geraStringAleatoria(tamanho) {
    var stringAleatoria = '';
    var caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (var i = 0; i < tamanho; i++) {
        stringAleatoria += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
    }
    return stringAleatoria;
}
</script>

{% endblock %}

