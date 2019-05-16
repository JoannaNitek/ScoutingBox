
$('#table').bootstrapTable({
  url: 'data1.json',
  pagination: true,
  columns: [{
    field: 'id',
    title: '#'
  }, {
    field: 'name',
    title: 'Imię i nazwisko'
  }, {
    field: 'year',
    title: 'Rocznik'
  }, {
    field: 'club',
    title: 'Klub'
  }, {
    field: 'position',
    title: 'Pozycja'
  }, {
    field: 'status',
    title: 'Status'
  }, {
    field: 'agent',
    title: 'Agent'
  }, {
    field: '1',
    title: 'Uwagi'
  }, {
    field: '2',
    title: 'Uwagi'
  }, {
    field: '3',
    title: 'Uwagi'
  }]
});