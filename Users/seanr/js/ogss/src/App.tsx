import styled, { createGlobalStyle } from 'styled-components';

import CardGrid from './card-grid';

const App = () => {
  return (
    <StyledMain>
      <GlobalStyle />
      <CardGrid />
    </StyledMain>
  );
}

export default App;

const GlobalStyle = createGlobalStyle`
  * {
    font-family: 'Noto Sans KR', sans-serif;
  }
  
  body {
    margin: 0;
    padding: 0;
    background: #0e0d1c;
  }
`;

const StyledMain = styled.div`
  height: calc(100vh - 60px);
  width: calc(100vw - 80px);
  position: relative;
  color: #f2f2f2;
  margin: 30px 40px;
  display: flex;
  justify-content: center;
  align-items: center;
`;
