var elementosAnos = document.querySelectorAll('.anos')

elementosAnos.forEach(function (anos){
  anos.addEventListener('click', function (){
   anos.classList.toggle('ativa')
  })
})