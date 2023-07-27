import { Box } from "@mui/material";

import { TextArea } from "./TextArea";

export const Chat = () => {
  return (
    <Box
      sx={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "space-between",
        height: "100vh",
        padding: "24px",
      }}
    >
      <Box>
        <p>
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae
          beatae molestiae temporibus numquam quia voluptatem, ipsa vero dolorum
          voluptas soluta, doloribus dolorem accusantium tempora magnam delectus
          sed unde corrupti? Repellat.
        </p>
      </Box>
      <TextArea />
    </Box>
  );
};
