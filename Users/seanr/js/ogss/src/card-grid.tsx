import styled, { keyframes } from 'styled-components';

import { jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec } from './srcs';
import Card from './card';

const CardGrid = () => {
  return (
    <StyledGrid>
      <Card src={jan[0]} />
      <div />
      <Card src={mar[0]} />
      <div />
      <div />
      <div />
      <div />
      <Card src={aug[0]} />
      <div />
      <div />
      <Card src={nov[0]} />
      <Card src={dec[0]} />
      <Card src={jan[1]} />
      <Card src={feb[0]} />
      <Card src={mar[1]} />
      <Card src={apr[0]} />
      <Card src={may[0]} />
      <Card src={jun[0]} />
      <Card src={jul[0]} />
      <div />
      <Card src={sep[0]} />
      <Card src={oct[0]} />
      <div />
      <Card src={dec[1]} />
      <div />
      <Card src={feb[1]} />
      <div />
      <Card src={apr[1]} />
      <Card src={may[1]} />
      <Card src={jun[1]} />
      <Card src={jul[1]} />
      <Card src={aug[1]} />
      <Card src={sep[1]} />
      <Card src={oct[1]} />
      <div />
      <Card src={dec[2]} />
      <Card src={jan[2]} />
      <Card src={feb[2]} />
      <Card src={mar[2]} />
      <Card src={apr[2]} />
      <Card src={may[2]} />
      <Card src={jun[2]} />
      <Card src={jul[2]} />
      <Card src={aug[2]} />
      <Card src={sep[2]} />
      <Card src={oct[2]} />
      <Card src={nov[1]} />
      <Card src={dec[3]} />
      <Card src={jan[3]} />
      <Card src={feb[3]} />
      <Card src={mar[3]} />
      <Card src={apr[3]} />
      <Card src={may[3]} />
      <Card src={jun[3]} />
      <Card src={jul[3]} />
      <Card src={aug[3]} />
      <Card src={sep[3]} />
      <Card src={oct[3]} />
      <Card src={nov[2]} />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <div />
      <Card src={nov[3]} />
    </StyledGrid>
  )
}

export default CardGrid;

const fadeIn = keyframes`
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
`;

const StyledGrid = styled.div<{}>`
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: repeat(6, 1fr);
  gap: 10px;
  animation: ${fadeIn} 1s ease-out;
`;
