import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FileSystemDirectoryEntry, FileSystemFileEntry, NgxFileDropEntry } from 'ngx-file-drop';
import { ClientService } from 'src/app/client.service';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent implements OnInit {

  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private route: Router
  ) { }

  estado: boolean = false;
  tabla(){
    this.estado = true;
  }

  hide: true;
  notification: boolean;
  dataEx: JSON;
  state: string;
  headers =["id", "Nombres", "Apellidos", "Fecha", "Eliminar"];
  rows = [];

  ngOnInit(): void {
    this.form = this.fb.group({
      file_a: ['', Validators.required],
      id_p: ['',Validators.required]
    });
  }

  public files: NgxFileDropEntry[] = [];

  public dropped(files: NgxFileDropEntry[]) {
    this.files = files;
    for (const droppedFile of files) {

      // Is it a file?
      if (droppedFile.fileEntry.isFile) {
        const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
        fileEntry.file((file: File) => {

          // Here you can access the real file
          console.log(droppedFile.relativePath, file);

          /**
          // You could upload it like this:
          const formData = new FormData()
          formData.append('logo', file, relativePath)

          // Headers
          const headers = new HttpHeaders({
            'security-token': 'mytoken'
          })
          **/
          this.client.postRequest('https://127.0.0.1:5000/authorization', {})
          .subscribe(data => {
            // Sanitized logo returned from backend
          })


        });
      } else {
        // It was a directory (empty directories are added, otherwise only files)
        const fileEntry = droppedFile.fileEntry as FileSystemDirectoryEntry;
        console.log(droppedFile.relativePath, fileEntry);
      }
    }
  }

  public fileOver(event){
    console.log(event);
  }

  public fileLeave(event){
    console.log(event);
  }

  async onSubmit(){
    if (this.form.valid) {
      this.rows = [];
      this.client.postRequest('http://127.0.0.1:5000/appointment',{
        reason: this.form.value.reason,
        date_a: this.form.value.date_a
      }).subscribe((response: any) => {
        console.log(response);
        this.form.reset();
      }),
      (error) => {
        console.log(error.status);
        this.route.navigate(['/patient'])

      };
    }else{
      console.log('Error en la entrada de datos del formulario del cliente');
      this.notification = true;

    }

  }

  delete(appointment:any, id_row:number){
    this.client.deleteRequest('http//127.0.0.1:5000/appointment', appointment['Id']).subscribe((data:any) => {
      this.dataEx = data;
      this.state = this.dataEx['state'];
      switch (this.state) {
        case 'ok':
          if (appointment['Id'] == this.rows[id_row]['Id']) {
            this.rows.splice(id_row, 1);
            this.tabla()
          }
          console.log('delete')
          break;
        case 'document':{
          console.log('Unregistred user')
          break;
        }
        case 'error': {
          console.log('error')
        }
      }
    });
  }

}
