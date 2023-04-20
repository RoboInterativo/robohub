import React, { useEffect,useState }  from "react";
import Grid from '@mui/material/Grid';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

// import Breadcrumbs from '@mui/material/Breadcrumbs';
// import Link from '@mui/material/Link';

// import SvgIcon from '@mui/material/SvgIcon';
// import { createSvgIcon } from '@mui/material/utils';
// import HomeIcon from '@mui/icons-material/Home';
// import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';
import TelegramIcon from '@mui/icons-material/Telegram';
import { styled } from '@mui/material/styles';
//
// import InsertDriveFileIcon from '@mui/icons-material/InsertDriveFile';
// import DownloadIcon from '@mui/icons-material/Download';
// import EditIcon from '@mui/icons-material/Edit';
// import FolderIcon from '@mui/icons-material/Folder';
//
// // import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Avatar from '@mui/material/Avatar';
// import IconButton from '@mui/material/IconButton';
// import DeleteIcon from '@mui/icons-material/Delete';
// import DeleteIcon from '@mui/icons-material/Delete';
// import ListItemAvatar from '@mui/material/ListItemAvatar';
// import Avatar from '@mui/material/Avatar';
// import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
// import ListItemIcon from '@mui/material/ListItemIcon';

// import ListItemText from '@mui/material/ListItemText';
// import FolderIcon from '@mui/icons-material/Folder';

// import { styled } from '@mui/material/styles';
//import Box from '@mui/material/Box';
// import Grid from '@mui/material/Grid';
// import Paper from '@mui/material/Paper';
// import Toolbar from '@mui/material/Toolbar';
// import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
// import Card from '@mui/material/Card';
// import CardActions from '@mui/material/CardActions';
// import CardContent from '@mui/material/CardContent';


 // import MailIcon from '@mui/icons-material/Mail';
// import StorageIcon from '@mui/icons-material/Storage';
// import CommentIcon from '@mui/icons-material/Comment';
// import IconButton from '@mui/material/IconButton';
// import AppsOutlinedIcon from '@mui/icons-material/AppsOutlined';

// import AddCircleIcon from '@mui/icons-material/AddCircle';
// import Button from '@mui/material/Button';
// import Table from '@mui/material/Table';
// import TableBody from '@mui/material/TableBody';
// import TableCell from '@mui/material/TableCell';
// import TableContainer from '@mui/material/TableContainer';
// import TableHead from '@mui/material/TableHead';
// import TablePagination from '@mui/material/TablePagination';
// import TableRow from '@mui/material/TableRow';
// import TableSortLabel from '@mui/material/TableSortLabel';
// import Container from '@mui/material/Container';
//import { ReactComponent as TGIcon } from './icons8-telegram-48.svg';
// import TGpng from './telegram.png';

import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme();



theme.typography.h2 = {
  fontSize: '1.0rem',
  '@media (min-width:600px)': {
    fontSize: '1.1rem',
  },
  [theme.breakpoints.up('md')]: {
    fontSize: '1.4rem',
  },
};



import axios from 'axios';


// const drawerWidth = 240;
//const data_auth= true;





function DashBoard () {
  // const [dashboard,setDashboard]= useState('servers');
//   const buttonClick = (dash) => () => {
//   // if (event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
//   //   return;
//   // }
//
//   setDashboard(dash);
// };

  // const [data]= useState(
  //   {"auth": true, "files": [{"modify_time": "2022-06-15 22:32:49", "is_dir": true, "name": "back", "size_str": "4.0 KB", "permiss": "drwxrwxr-x"}, {"modify_time": "2022-06-15 22:32:16", "is_dir": true, "name": ".cache", "size_str": "4.0 KB", "permiss": "drwx------"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": false, "name": ".gitignore", "size_str": "1.7568359375 KB", "permiss": "-rw-rw-r--"}, {"modify_time": "2022-06-15 22:29:49", "is_dir": true, "name": "front", "size_str": "4.0 KB", "permiss": "drwxrwxr-x"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": false, "name": "index.html", "size_str": "2.1435546875 KB", "permiss": "-rw-rw-r--"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": false, "name": "1", "size_str": "28 bytes", "permiss": "-rw-rw-r--"}, {"modify_time": "2022-06-15 22:27:47", "is_dir": true, "name": ".git", "size_str": "4.0 KB", "permiss": "drwxrwxr-x"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": false, "name": "README.md", "size_str": "21 bytes", "permiss": "-rw-rw-r--"}, {"modify_time": "2022-06-15 22:32:19", "is_dir": true, "name": ".local", "size_str": "4.0 KB", "permiss": "drwxr-xr-x"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": true, "name": "task2.1", "size_str": "4.0 KB", "permiss": "drwxrwxr-x"}]}
  //
  //
  // );




  const Demo = styled('div')(({ theme }) => ({
  backgroundColor: theme.palette.background.paper,
}));
  //const auth=true;
  const [data,setData]= useState('');
  useEffect ( () =>  {
    axios.post('/api/robos')
        .then(response => {
          console.log(response);
          setData(response.data)
          localStorage.setItem('auth',response.data.auth)
        })
        .catch(error => {
           console.error('There was an error!', error);
        });

  },[])

//   const Item = styled(Paper)(({ theme }) => ({
//   ...theme.typography.body2,
//   padding: theme.spacing(1),
//   textAlign: 'center',
//   color: theme.palette.text.secondary,
// }));
//  {JSON.stringify(data.files) }
  // setData({"auth": true, "files": [{"modify_time": "2022-06-15 22:32:49", "is_dir": true, "name": "back", "size_str": "4.0 KB", "permiss": "drwxrwxr-x"}, {"modify_time": "2022-06-15 22:32:16", "is_dir": true, "name": ".cache", "size_str": "4.0 KB", "permiss": "drwx------"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": false, "name": ".gitignore", "size_str": "1.7568359375 KB", "permiss": "-rw-rw-r--"}, {"modify_time": "2022-06-15 22:29:49", "is_dir": true, "name": "front", "size_str": "4.0 KB", "permiss": "drwxrwxr-x"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": false, "name": "index.html", "size_str": "2.1435546875 KB", "permiss": "-rw-rw-r--"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": false, "name": "1", "size_str": "28 bytes", "permiss": "-rw-rw-r--"}, {"modify_time": "2022-06-15 22:27:47", "is_dir": true, "name": ".git", "size_str": "4.0 KB", "permiss": "drwxrwxr-x"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": false, "name": "README.md", "size_str": "21 bytes", "permiss": "-rw-rw-r--"}, {"modify_time": "2022-06-15 22:32:19", "is_dir": true, "name": ".local", "size_str": "4.0 KB", "permiss": "drwxr-xr-x"}, {"modify_time": "2022-05-25 06:46:10", "is_dir": true, "name": "task2.1", "size_str": "4.0 KB", "permiss": "drwxrwxr-x"}]})
  return (
    <div>



      { !data.auth &&
        <div>
          <p>Forbidden</p>
        </div>
      }
      { data.auth &&
          <div>
          <Grid container spacing={3}>
            {/* Chart */}
            <Grid item xs={12} md={8} lg={9}>
            <Paper
              sx={{
                p: 2,
                display: 'flex',
                height: '800px',
                flexDirection: 'column',
                maxWidth: '800px',
                width: '800px',






              }}
            >



<ThemeProvider theme={theme}>
    <Typography variant="h2" >
    Telegram
    </Typography>

<List dense={true}
  component="nav"
  sx={{ height: 'auto',
    maxWidth: '800px',
    fontSize: 14,
    overflow: 'auto',
    width:'800px',
    display: 'flex',
    flexWrap: 'wrap',
    alignItems: 'flex-start',
    padding: 0,
    position: 'relative',}}
     >

  { data && data.robos.map((item)=>
    <Demo key={item.id} >
    <ListItem   sx= {{ width:'300px' }}>

     <ListItemButton   sx={{ p: 2, border: '1px solid grey' }} item xs={4}>
    <ListItemAvatar>
          <Avatar>
          <TelegramIcon color="primary"  />
          </Avatar>
        </ListItemAvatar>

 <ListItemText primary={item.titulo} secondary="не привязан" />
       </ListItemButton>


    </ListItem>
      </Demo>)
  //</a target="_blank" href="https://icons8.com/icon/13977/вконтакте">ВКонтакте</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
//<a target="_blank" href="https://icons8.com/icon/108842/viber">Viber</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
//<a target="_blank" href="https://icons8.com/icon/RLJfWOxNk8Bc/discord">Discord</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
    // <ListItem>
    // <ListItemButton item xs={4}>
    //
    //   <IconButton  sx={{ color: '#888' ,width: 40,fontSize:'10px'}}  edge="start" aria-label="delete"> {item.is_dir ?<FolderIcon />:<InsertDriveFileIcon />} </IconButton>
    //     <ListItemText item xs={4}  sx={{ width: 150}}             primary=<div>{item.name}</div>             />
    //     </ListItemButton>
    //
    //     <IconButton  sx={{ color: '#888' ,width: 40,fontSize:'10px'}}  edge="end" aria-label="delete"> <DownloadIcon /> </IconButton>
    //     <IconButton sx={{ color: '#888' ,width: 40,fontSize: '10px'}}  edge="end" aria-label="delete"> <EditIcon /> </IconButton>
    //     <IconButton  sx={{ color: '#888' ,width: 40,fontSize:'10px'}}  edge="end" aria-label="delete"> <DeleteIcon /> </IconButton>
    //     <ListItemText   item xs={4} sx={{  fontSize: '13px' ,color: '#888' , width: 150}}                primary=<div>{" "+item.modify_time +"  "+item.size_str}</div>             />
    // </ListItem>

}
</List>
<Typography variant="h2" >
Viber
</Typography>
<Typography variant="body1" >
Нет ботоа
</Typography>
<Typography variant="h2" >
VK
</Typography>
<Typography variant="body1" >
Нет ботоа
</Typography>
  </ThemeProvider>
    </Paper>

            </Grid>



          </Grid>


        </div>    }

</div>
)}



export default  DashBoard;
