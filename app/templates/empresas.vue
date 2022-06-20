{% extends "base.html" %}
{% block content %}
<style>
#nav-top{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
#btn-adicionar{
  width: 35px;
  height: 35px;
  background-color: blue;
  color: white;
  font-size: 20px;
  cursor: pointer;
  border-radius: 6px;
  border: none;
  margin-right: 30px;
}
.card{
  width: 100%;
  height: 100px;
  border-radius: 5px;
  box-shadow: 4px 4px 12px -4px rgba(0,0,0,0.67);
  color: black;
  grid-column: 1 span;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  transition: all .5s;

}
#grid-card{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  width: 100%;
  height: auto;
  margin-top: 30px;
  gap: 10px;
}
#input_search{
  width: 350px;
  padding: 15px;
  font-size: 15px;
  border-radius: 6px;
  border: 1px solid;
}
a{
  text-decoration: none;
}
.card:hover{
    background-color: rgb(0, 255, 98);
    color: white;
  
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

<template id="vue-app">
<div>
        <div>
      <div id="nav-top" > 
          <h1>Empresas</h1>
          <div>
              <span>Caio</span>
          </div>
      </div>
      <hr>
        <h2 style="margin-top: 50px;">Lista de empresas cadastradas</h2>
              <div id="nav-top" style="margin-top: 10px;">
                    <div>
                    <input type="text" 
                    id="input_search"
                    placeholder="Digite o nome da Empresa ou CNPJ"
                    v-model="textSearch"
                    @keyup="search()"
                    >
                    <i style="margin-left: -30px;" class="fa-solid fa-magnifying-glass"></i>
                    </div>
                    <div style="display: flex; flex-direction: row; align-items: center; gap: 10px;" >
                      <h3>Adicionar nova empresa</h3>
                      <input type="button" id="btn-adicionar" onclick="javascript:location.href=`/empresas/cadastro`" value="+">
                  </div>
              </div>
    </div>

    <div id="grid-card" >
      <div v-for="card in dadosFiltrer" :key="card.id_empresa">
        <card :post-Title='card.nome' :id='card.id_empresa' :cnpj="card.cnpj"></card>
        
      </div>


    </div>
</div>
</template>



<template id='card'>
         <a v-bind:href='"empresas/editar/" + id'>
            <div class='card'>
                <h1>${postTitle}</h1>
                <span>Cnpj: ${cnpj}</span>
                <div>
                
                </div>
            </div>
          </a>
</template>

   
  <script type="text/javascript">

// -----------------Card Componente---------------
    Vue.component('card', {
        template: '#card',
        props: ['postTitle',
                'id',
                'cnpj',
        ],
        delimiters: ['${', '}']

      },
    )

    new Vue({ 
      el: "#vue-app", 
      data(){
          return {
            dados: [],
            textSearch: '',
            dadosFiltrer: [],
          }
      },
      async mounted(){
        const res = await fetch('empresas/cadatros/numID')
        const data = await res.json()
        this.dados = data
        this.dadosFiltrer = data
      },
      methods: {
        search(){
           this.dadosFiltrer = this.dados.filter(dados =>
                       dados.nome.toLowerCase().includes(this.textSearch.toLowerCase()) ||
                        dados.cnpj.includes(this.textSearch)
            );
        }
      }
    }); 
         
  </script>
{% endblock content %}
