import { useState } from "react"
import "../index.css"

function FileUpload({handleImage, fileUpload}){
    
        
    return(
        <div className="relative flex gap-8 items-center">

            <div>
                <p className="green-fonts-escuro text-xl">Choose your files</p>
            </div>
            <div className="relative flex">
                <button className="green-light-background green-fonts-escuro py-2 px-8 rounded-sm font-medium text-lg">Upload</button>
                <input
                className="opacity-0 absolute w-full"
                onChange={handleImage}
                type="file" />
            </div>

            <button className="button-enviar py-2 px-8 rounded-sm text-lg"
            onClick={fileUpload}
            >Enviar</button>
        </div>
    )
}

export default FileUpload