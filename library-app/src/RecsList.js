import React, {useState, useEffect} from 'react';

function RecsList() {
    const [recs, setRecs] = useState([])

    useEffect(() => {
        fetch('/api/recs').then(res => res.json())
        .then(data => {
            setRecs(data.books)
            console.log("data here: ", recs)
        }).catch((error) => console.error('Error: ', error))
    }, [])

    return (
        <>
            <h2>Recommendations</h2>
            <div className="recsList">
                {(typeof recs === undefined) ? (
                    <p>Loading...</p>
                    ) : (
                        recs.map((book) => (<p>{book}</p>))
                        )}
            </div>
            <p>hello</p>
        </>
    )
}

export default RecsList