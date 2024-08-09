import ReadBooks from './ReadBooks';
import RecsList from './RecsList';

function App() {
  return (
    <>
      <h1 className="title">Personal Library App</h1>
      <div className='content'>
        <ReadBooks />
        <RecsList />
      </div>
    </>
  );
}

export default App;
