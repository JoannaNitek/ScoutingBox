
$('#table2').bootstrapTable({
  url: 'data1.json',
  pagination: true,
  columns: [{
    field: 'date',
    title: 'Data i godzina'
  }, {
    field: 'match',
    title: 'Mecz'
  }, {
    field: 'city',
    title: 'Lokalizacja'
  }, {
      field: 'scout',
      title: 'Obserwujący'
  }]});