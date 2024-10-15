import Nav from "../components/Nav"
import '../index.css'


import { useState } from 'react'

function Retults(){

    const filename = localStorage.getItem('filename');
    const [url, setUrl] = useState('')

    fetch("http://127.0.0.1:8000/results/"+filename,{
    }).then((response) => {
        console.log(response, 'respnse')
        setUrl(response.url)
    })

    return(
        <div>
            <header>
                <Nav/>
            </header>


            {/* resultado container */}
            <div className="flex mx-32 items-center justify-center gap-x-28 mt-28">
                {/* imagem  */} 
                <div className="w-2/5">
                    <img
                    className="w-full"
                    src={url} alt="" />
                </div>

                {/* resultado */}
                <div className=" flex flex-col w-1/3">
                    <div>
                        <h2 className="text-center green-fonts-escuro font-semibold text-2xl">Results</h2>
                    </div>

                    <div className="px-10 py-8 gap-y-10 mt-6 rounded green-text-results">

                        <div className="flex justify-between border-b border-b-slate-200 pb-6 font-medium">
                            <p>Unhealthy</p>
                            <p className="mr-3">0</p>
                        </div>

                        <div className="flex justify-between mt-6 font-medium">
                            <p>healthy</p>
                            <p className="mr-3">0</p>
                        </div>
                    </div>

                    <div className="text-center mt-6 green-text-results font-medium">
                        <p>Upload new image <span className="green-text">here</span></p>
                    </div>
                </div>

            </div>
        </div>
    )
}

export default Retults