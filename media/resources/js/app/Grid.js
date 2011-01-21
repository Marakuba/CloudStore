// Create a standard HttpProxy instance.
var proxy = new Ext.data.HttpProxy({
    url: '/api/users'
});

// Typical JsonReader.  Notice additional meta-data params for defining the core attributes of your json-response
var reader = new Ext.data.JsonReader({
    totalProperty: 'total',
    successProperty: 'success',
    idProperty: 'id',
    root: 'data',
    messageProperty: 'message'  // <-- New "messageProperty" meta-data
}, [
    {name: 'id'},
    {name: 'email', allowBlank: false},
    {name: 'first_name', allowBlank: false},
    {name: 'last_name', allowBlank: false}
]);

// The new DataWriter component.
var writer = new Ext.data.JsonWriter({
    encode: false   // <-- don't return encoded JSON -- causes Ext.Ajax#request to send data using jsonData config rather than HTTP params
});

// Typical Store collecting the Proxy, Reader and Writer together.
var store = new Ext.data.Store({
    id: 'user',
    restful: true,     // <-- This Store is RESTful
    proxy: proxy,
    reader: reader,
    writer: writer    // <-- plug a DataWriter into the store just as you would a Reader
});

// load the store immeditately
//store.load();


// Let's pretend we rendered our grid-columns with meta-data from our ORM framework.
var userColumns =  [
    {header: "ID", width: 40, sortable: true, dataIndex: 'id'},
    {header: "Email", width: 100, sortable: true, dataIndex: 'email', editor: new Ext.form.TextField({})},
    {header: "First", width: 50, sortable: true, dataIndex: 'first', editor: new Ext.form.TextField({})},
    {header: "Last", width: 50, sortable: true, dataIndex: 'last', editor: new Ext.form.TextField({})}
];

var userGrid = new Ext.grid.GridPanel({
    iconCls: 'icon-grid',
    frame: true,
    title: 'Users',
    height: 300,
    store: store,
    columns : userColumns,
    tbar: [{
        text: 'Add',
        iconCls: 'silk-add',
        handler: onAdd
    }, '-', {
        text: 'Delete',
        iconCls: 'silk-delete',
        handler: onDelete
    }, '-'],
    viewConfig: {
        forceFit: true
    }
});


