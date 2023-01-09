import { useState, useEffect, useRef } from 'react';
import styled from 'styled-components';

type PropsType = {
  src: string,
};

const target = 100 / 61;

const Card = (props: PropsType) => {
  const [loaded, setLoaded] = useState(false);
  const [rect, setRect] = useState<DOMRect>();
  const [width, setWidth] = useState(0);
  const [height, setHeight] = useState(0);

  const wrapperRef = useRef<HTMLDivElement>(null);

  const updateRect = () => {
    if (!loaded && wrapperRef.current !== undefined) {
      setRect(wrapperRef.current!.getBoundingClientRect());
    }
  }

  useEffect(() => {
    window.addEventListener('resize', updateRect);
    return () => window.removeEventListener('resize', updateRect);
  }, []);

  useEffect(() => {
    const getDims = () => {
      if (rect) {
        let h;
        let w;
        if (rect.height/ rect.width < target) {
          h = rect.height;
          w = h / target;
        } else {
          w = rect.width;
          h = target * w;
        }
        setHeight(h);
        setWidth(w);
        console.log(h, w);
        setLoaded(true);
      }
    }
    
    getDims();
  }, [rect]);

  useEffect(() => {
    updateRect();
  }, [wrapperRef.current]);

  return (
    <CardWrapper ref={wrapperRef}>
      {loaded && <StyledImg src={props.src} w={width} h={height} />}
    </CardWrapper>
  );
}

export default Card;

const CardWrapper = styled.div`
  max-width: 100%;
  max-height: 100%;
  padding: 0;
  margin: 0;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const StyledImg = styled.img<{ w: number, h: number }>`
  width: ${(props) => props.w}px;
  height: ${(props) => props.h}px;
`;
