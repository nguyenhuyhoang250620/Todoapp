import React,{useState,useEffect} from 'react';
import {
  SafeAreaView,
  StyleSheet,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  FlatList,
  Alert
} from 'react-native';
import Icon from 'react-native-vector-icons/MaterialIcons';
import AsyncStorage from '@react-native-async-storage/async-storage';


const COLOR = {primary:"#1f145c",white:"#fff"}
const App =() => {

  const [textinput,setTextinput] = useState('')
  const [todos,setTodos] = useState([])

  useEffect(()=>{
    getTodo();
  },[])

  useEffect(()=>{
    saveTodo(todos);
  },[todos])



  // thêm list công việc
  const addtodo=()=>{
    if (textinput == '') {
      Alert.alert("Lỗi","Cần nhập dữ liệu")
    } else {
      const newtodo = {
        id:Math.random(),
        task:textinput,
        complete:false
      }
      setTodos([...todos,newtodo])
      setTextinput('')
    }
  }
  //Lưu vào bộ nhớ 
  const saveTodo = async todolist=>{
    try {
      const stringfytodo = JSON.stringify(todolist);
      await AsyncStorage.setItem('todolist',stringfytodo);
    } catch (error) {
      console.log(error)
    }
  }

  //lấy dữ liệu
  const getTodo = async ()=>{
    try {
      const todos = await AsyncStorage.getItem('todolist')
      if(todos != null){
        setTodos(JSON.parse(todos))
      }
    } catch (error) {
      console.log(error)
    }
  }

  //tích công việc đã hoàn thành
  const completeTodos=(todoID)=>{
    const newtodo = todos.map(item=>{
      if(item.id==todoID){
        return{...item,complete:true}
      }
      return item;
    });
    setTodos(newtodo)
  }

  //xoá công việc
  const deteletodo = (todoID)=>{
    const newtodo = todos.filter(item=>item.id != todoID);
    setTodos(newtodo)
  }
  //xoá tất cả
  const clear = ()=>{
    if (todos.length===0) {
      Alert.alert("Lỗi","không có gì để xoá")
    } else {
      Alert.alert("Xoá tất cả","Bạn có chắc muốn xoá không",[
        {
          text:"Có",
          onPress:()=>setTodos([])
        },
        {
          text:"Không"
        }
      ])
    }
  }

  //hiển thị ra list công việc
const ListItem = ({todo})=>{
  return(
    <View style={styles.listItem}>
      <View style={{flex:1,}}>
        <Text style={{
          fontWeight:"bold",
          fontSize:15,
          color:COLOR.primary,
          textDecorationLine:todo.complete ? 'line-through':'none'
          }}>{todo.task}</Text>
      </View>
      {
        !todo.complete &&
        <TouchableOpacity onPress={()=>completeTodos(todo.id)}>
          <View style={[styles.actionIcon,{marginRight:5}]}>
            <Icon name='done' size={20} color={COLOR.white}/>
          </View>
        </TouchableOpacity>
      }
      <TouchableOpacity onPress={()=>deteletodo(todo.id)}>
        <View style={[styles.actionIcon,{backgroundColor:"red"}]}>
          <Icon name='delete' size={20} color={COLOR.white}/>
        </View>
      </TouchableOpacity>
    </View>
  )
}
  
  return (
    <SafeAreaView style={{flex:1,backgroundColor:COLOR.white}}>
      <View style={styles.header}>
        <Text style={styles.title}>TODO APP</Text>
        <Icon onPress={clear} name="delete" size={25} color="red"/>
      </View>
      <FlatList
        data={todos}
        contentContainerStyle={{padding:10}}
        showsVerticalScrollIndicator={false}
        renderItem={({item})=><ListItem todo={item} />}
        keyExtractor={item => item.id.toString()}
      />
      <View style={styles.footer}>
        <View style={styles.inputContainer}>
          <TextInput 
            placeholder='add todo' 
            value={textinput}
            onChangeText={texts=>setTextinput(texts)}
          />
        </View>
        <TouchableOpacity onPress={addtodo}>
          <View style={styles.iconContainer}>
            <Icon name='add' color={COLOR.white} size={25} />
          </View>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
};
const styles= StyleSheet.create({
  header:{
    padding:20,
    justifyContent:"space-between",
    alignItems:"center",
    flexDirection:"row",
    borderBottomWidth:2,
    backgroundColor:"yellow"
  },
  title:{
    fontWeight:"bold",
    fontSize:20,
    color:"black"
  },
  footer:{
    position:'absolute',
    bottom:0,
    alignItems:"center",
    flexDirection:"row",
    width:'100%',
    paddingHorizontal:20,
    color:COLOR.white
  },
  inputContainer:{
    backgroundColor:COLOR.white,
    elevation:40,
    flex:1,
    height:50,
    marginVertical:20,
    marginRight:20,
    borderRadius:30,
    paddingHorizontal:20
  },
  iconContainer:{
    height:50,
    width:50,

    backgroundColor:COLOR.primary,
    borderRadius:25,
    elevation:40,
    justifyContent:"center",
    alignItems:"center"
  },
  listItem:{
    padding:20,
    backgroundColor:COLOR.white,
    flexDirection:"row",
    elevation:20,
    borderRadius:7,
    marginVertical:10
  },
  actionIcon:{
    height:20,
    width:20,
    backgroundColor:"green",
    justifyContent:"center",
    alignItems:"center",
    marginLeft:5,
    borderRadius:3
  }
})
export default App;
