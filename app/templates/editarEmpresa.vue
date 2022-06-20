{% extends 'base.html' %} 
{% block content %}

{% load crispy_forms_tags %}
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,700;1,500&display=swap');

*{
font-family: 'Roboto', sans-serif;
}
input{
  width: 50%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
  width: 400px;
}
label,input{
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}
.id_empresa{
    width: 100px;
}
.cadata{
    width: 50%;
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
.div_btn{
  position: relative;
  bottom: 0;
  left: 40%;
}

hr{
    margin-bottom: 10px;
}
.flex-row{
  display: flex;
  flex-direction: row;
  align-items: center; gap: 10px;
}
.flex-colum{
  display: flex;
  flex-direction: column;
}
#btn-add{
    width: 100px;
    margin-top: 25px;
    cursor: pointer;
    background-color: aqua;
    border: 1px solid white;
    color: white;
    border-radius: 6px;
}
#thead, #tbody{
  width: 100%;
  display: flex;
  flex-direction: row;
  padding-left: 1rem;
  padding-right: 1rem;
}
#thead{
  justify-content: space-between;

}
#tbody{
  margin-top: 10px;
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

</style>


  <div ></div>
  <div >
    <form action="" method="POST" autocomplete="off">
      {% csrf_token %}

      {% crispy form %}

    </form>
  </div>

<template id="app">
  <div class='table'>
    <h3>Adicionar colaboradores:</h3>
    <hr>
    <div class="flex-row">
          <div class="flex-colum">
            <label for="">Nome*</label>
            <input type="text" id="nome">
          </div>

          <div class="flex-colum">
            <label for="">Cpf*</label>
            <input type="text" id="cpf">
          </div>

           <div class="flex-colum">
            <label for="">Email</label>
            <input type="text" id="email">
          </div>
    </div>
      <div class="flex-row">
        <div class="flex-colum">
            <label for="">Telefone</label>
            <input type="text" id="telefone">
          </div>
          <div class="flex-colum">
            <label for="">Endereço</label>
            <input type="text" id="endereco">
          </div>
          <input type="button" id="btn-add" onclick="addColaborador()" v-on:click="buscar"  value="Adicionar" >
      </div>
          <h3>Lista de colaboradores:</h3>
         <hr>
          <div id='thead'>
          <span style="width:25%">Nome</span>
          <span style="width:25%">CPF</span>
          <span style="width:25%">Email</span>
          <span style="width:25%">Telefone</span>
          <span >Ações</span>

      </div>
         <div v-for="card in dadosFunc" :key="card.id_colaborador">
         <colaborador :nome='card.nome'
          :cpf='card.cpf'
          :email='card.email'
          :telefone='card.telefone'
          :id="card.id_colaborador"
          />
        
      </div>
    <a class="btn-retornar"  style="margin-top: 30px;" :href='"remover/"+ idEmpresa'>Deletar Empresa</a>

</div>


</template>

<template id="colaborador-card">


      <div id='tbody'>
          <span style="width:25%">${nome}</span>
          <span style="width:25%">${cpf}</span>
          <span style="width:25%">${email}</span>
          <span style="width:25%">${telefone}</span>
          <a :href="'javascript:removeColab('+id+');'"><i style="color:red;" class="fa-solid fa-trash-can"></i></a>


      </div>

</template>

<script>
    $(document).ready( function  (){
        document.getElementById('id_id_empresa').readOnly = true; 
   })

    //------------------Adicionar Colaborador---------------
    function addColaborador(){
       var nome = $('#nome').val();
       var  cpf = $('#cpf').val();
       var  email = $('#email').val();
       var  telefone = $('#telefone').val();
       var  endereco = $('#endereco').val();
       var empresa = $('#id_nome').val()
       var id = $('#id_id_empresa').val()

       if(email == '')
          email = 'ND'
       if(telefone == '')
          telefone = 'ND'
       if(empresa == '')
          empresa = 'ND'
       if(endereco == '')
          endereco = 'ND'

        fetch(`colaborador/${cpf}/${nome}/${email}/${telefone}/${endereco}/${empresa}/${id}`)
        location.reload();

    }
        //------------------Fim---------------



    function removeColab(id){
          fetch(`api/remove/${id}`)
          location.reload();
    }


    Vue.component('colaborador', {
        template: '#colaborador-card',
        props: [
          'nome',
          'cpf',
          'email',
          'telefone',
          'id'
        ],
        delimiters: ['${', '}']

      },
    )

    new Vue({ 
      el: "#app", 
      data(){
          return {
            dadosFunc: [],
            idEmpresa: $('#id_id_empresa').val(),
          }
      },
      async mounted(){
          this.buscar()
      },
      methods: {
          buscar: async function(){
              var id = $('#id_id_empresa').val()
              const res = await fetch(`api/${id}`)
              const data = await res.json()
              this.dadosFunc = data
          }
      },
    });
 

    


</script>

{% endblock %}

