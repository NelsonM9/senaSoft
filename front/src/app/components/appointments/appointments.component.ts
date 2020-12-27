import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ClientService } from '../../client.service';

@Component({
  selector: 'app-appointments',
  templateUrl: './appointments.component.html',
  styleUrls: ['./appointments.component.css']
})
export class AppointmentsComponent implements OnInit {

  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private route: Router
  ) { }

  estado: boolean = false;
  tabla() {
    this.estado = true;
  }

  hide: true;
  notification: boolean;
  dataEx: JSON;
  state: string;
  headers = ["Fecha", "Id Cita", "Id Doctor", "Id Paciente", "Razon", "Generar Cita"];
  rows = [];

  ngOnInit(): void {
    this.form = this.fb.group({
      reason: ['', Validators.required],
      id_p: ['', Validators.required],
      date_a: ['', Validators.required]
    });
  }

  async onSubmit() {
    if (this.form.valid) {
      setTimeout( () =>{
        this.rows = [];
        this.client.postRequest('http://127.0.0.1:5000/appointment', {
          reason: this.form.value.reason,
          id_p: this.form.value.id_p,
          date_a: this.form.value.date_a,
          id_a: '13',
          id_d: '1096145365'
        }).subscribe((response: any) => {
          this.dataEx = response;
          for (var j in this.dataEx['appointments']) {
            this.rows.push(this.dataEx['appointments'][j]);
          }
          console.log(response);
          this.form.reset();
        }),
          this.client.getRequest('http://127.0.0.1:5000/appointment',
            this.form.value.id_p
          ).subscribe((response: any) => {
            this.dataEx = response;
            console.log(this.dataEx)
            for (var i in this.dataEx) {
              for (var j in this.dataEx[i]) {
                this.rows.push(this.dataEx[i][j]);
              }
            }
            this.tabla()
            this.form.reset();
          }),
          (error) => {
            console.log(error.status);
            this.route.navigate(['/patient'])
          };
      }, 4000)
    } else {
      console.log('Error en la entrada de datos del formulario del cliente');
      this.notification = true;
    }
  }

  delete(appointment: any, id_row: number) {
    this.client.deleteRequest('http//127.0.0.1:5000/appointment', appointment['Id']).subscribe((data: any) => {
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
        case 'document': {
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
