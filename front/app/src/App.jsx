import { useState } from 'react'
import './App.css'
import Nav from './components/Nav'
import FileUpload from './components/FileUpload'
import UploadArea from './components/Upload_area'

import { useNavigate } from 'react-router-dom'

function App() {

  const navigate = useNavigate()

  const [image, setImage] = useState('')
  const [imageName, setImageName] = useState('')

    function handleImage (e){
        setImage(e.target.files[0])
    }

    

    function fileUpload(){
      const formData = new FormData();
      
      formData.append(
        'file',
        image,
      )
      
      fetch("http://127.0.0.1:8000/upload/",{
        method: 'POST',
        body: formData
        
      }).then(response=>{
        return response.json()

      }).then(data => {
        // const data = response.json()
        localStorage.setItem('filename', data.filename) 
        console.log(data.filename, 'hahahaha')
        setImageName(data.filename, 'name')
        console.log(data, 'hihihih')
        // setImage(response, 'haha')
        setImage(data.path)
        return data; 
      })
      navigate('/results')
    }

  return (
    <div>
      <Nav/>
      <div className='mx-48 flex flex-col items-center' >
        <UploadArea
        imagemName={imageName}
        imagem={image}
        />
        <FileUpload
        fileUpload={fileUpload}
        handleImage={handleImage}
        />

      </div>
    </div>
  )
}

export default App
