import upload from '../imgs/icon-upload-2 (1).svg'
import { useEffect, useState } from "react"
import '../index.css'
import imageUpload from '../imgs/icon-upload-2.svg' 

function UploadArea({ imagem, imagemName}){
    const [image, setImage] = useState('')
    const [imageName, setImageName] = useState('')

    useEffect(()=>{

        if (imagem){
            setImageName(imageName)
            console.log(imagemName, 'teste')
            setImage(imagem)
            console.log(image, 'image')
        }
    }, [imagem])
   
    // console.log(image, 'haha')

    return(
        <div className='green-background border-dashed border-2 border-spacing-6 border-color flex justify-center items-center container-upload my-16 w-3/4 gap-3 rounded-md'
        style={{
            backgroundImage: `url(${image})`,
            backgroundRepeat: 'no-repeat'
        }}>
            <div className='flex flex-col gap-6'>
                <div className='flex justify-center'>
                    <img src={imageUpload} alt="" />
                </div>
                <div className='mt-7'>
                    <p className='gray font-normal'>File supported<span className='green-text font-medium'> JPG, PNG, JPEG</span></p>
                </div>

            </div>
        </div>
    )
}

export default UploadArea