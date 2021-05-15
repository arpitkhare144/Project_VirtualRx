var pName,aadhar,opd,weight,age;

var pData,pData2,pData2Enc;
pData = {}


function getInput() {
    pName = document.getElementById("pName").value;
    aadhar = document.getElementById("aadhar").value;
    opd = document.getElementById("opd").value;
    weight = document.getElementById("weight").value;
    age = document.getElementById("age").value;
    console.log("Patient",pName);
    console.log("Age",age);
    console.log("Aadhar",aadhar);
    console.log("OPD",opd);
    console.log("Weight",weight);
    pData = {"pName":pName,"age":age,"aadhar":aadhar,"opd":opd,"weight":weight};
    pData2 = JSON.stringify(pData);
    pData2Enc = btoa(pData2);
    console.log(pData);
    console.log(typeof(pData2));
    console.log(pData2);
    console.log(pData2Enc)
    window.open("/register?monitor=2&data="+pData2Enc,'_self');
}

function monitor() {
    pName = document.getElementById("pName").value;
    aadhar = document.getElementById("aadhar").value;
    opd = document.getElementById("opd").value;
    weight = document.getElementById("weight").value;
    age = document.getElementById("age").value;
    pData = {"pName":pName,"age":age,"aadhar":aadhar,"opd":opd,"weight":weight};
    pData2 = JSON.stringify(pData);
    pData2Enc = btoa(pData2);
    console.log(pData);
    console.log(typeof(pData2));
    console.log(pData2);

    window.open("/register?monitor=1&data="+pData2Enc,'_self');
}

function submit() {

    window.open("/register/"+aadhar);
       console.log(pData);
    console.log(typeof(pData2));
    console.log(pData2);

}
