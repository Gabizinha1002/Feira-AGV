var elementosMaterias = document.querySelectorAll('.materias')

elementosMaterias.forEach(function (materias){
  materias.addEventListener('click', function (){
   materias.classList.toggle('ativa')
  })
})