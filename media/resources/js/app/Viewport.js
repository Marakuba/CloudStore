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
    id: 'users',
    restful: true,     // <-- This Store is RESTful
    proxy: proxy,
    reader: reader,
    writer: writer    // <-- plug a DataWriter into the store just as you would a Reader
});


// Let's pretend we rendered our grid-columns with meta-data from our ORM framework.
var userColumns =  [
    {header: "ID", width: 40, sortable: true, dataIndex: 'id'},
    {header: "Email", width: 100, sortable: true, dataIndex: 'email', editor: new Ext.form.TextField({})},
    {header: "First", width: 50, sortable: true, dataIndex: 'first_name', editor: new Ext.form.TextField({})},
    {header: "Last", width: 50, sortable: true, dataIndex: 'last_name', editor: new Ext.form.TextField({})}
];

var userGrid = new Ext.grid.GridPanel({
    border: false,
    //iconCls: 'icon-grid',
    title: 'Пользователи',
    store: store,
    columns : userColumns,
    tbar: [{
            xtype: 'buttongroup',
            title: 'Реализация',
            columns: 1,
            defaults: {
                scale: 'small'
            },
            items: [{
                //xtype:'splitbutton',
                text: 'Розница',
                iconCls: 'add16',
                //menu: [{text: 'Menu Item 1'}]
            },{
                //xtype:'splitbutton',
                text: 'Опт',
                iconCls: 'add16',
                //menu: [{text: 'Cut Menu Item'}]
            },{
                text: 'Журнал',
                iconCls: 'add16'
            }]
        },{
            xtype: 'buttongroup',
            title: 'Other Bogus Actions',
            columns: 2,
            defaults: {
                scale: 'small'
            },
            items: [{
                xtype:'splitbutton',
                text: 'Menu Button',
                iconCls: 'add16',
                menu: [{text: 'Menu Button 1'}]
            },{
                xtype:'splitbutton',
                text: 'Cut',
                iconCls: 'add16',
                menu: [{text: 'Cut Menu Item'}]
            },{
                text: 'Copy',
                iconCls: 'add16'
            },{
                text: 'Paste',
                iconCls: 'add16',
                menu: [{text: 'Paste Menu Item'}]
            },{
                text: 'Format',
                iconCls: 'add16'
            }]
        }]
,
    viewConfig: {
        forceFit: true
    }
});


Ext.onReady(function(){
    
    store.load();
    
    var viewport = new Ext.Viewport({
        layout: 'border',
        items: [
            new Ext.BoxComponent({ // raw element
                region:'north',
                el: 'header',
                height:32
            }),
            new Ext.TabPanel({
                region:'center',
                border:true,
                activeTab: 0,
                margins: '0 5 5 0',
                items: [
                    userGrid,
                ]
            }),
            new Ext.tree.TreePanel({
                region:'west',
                margins: '0 0 5 5',
                root: new Ext.tree.AsyncTreeNode({
                    text:'Главная панель',
                    children:[
                        {
                            text:'Справочники',
                            children: [
                                {
                                    text: 'Пользователи',
                                    leaf: true,
                                    iconCls: 'silk-group'
                                }
                            ]
                        }
                    ]
                }),
                width:250,
                split:true,
                rootVisible:false,
                lines:false,
                collapsible: true,
                collapseMode:'mini',
                header: false,
                tbar: [' ', new Ext.form.TextField({
                    width:200,
                })]
            })
        ],
    });
});